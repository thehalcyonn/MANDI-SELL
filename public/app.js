/**
 * MandiSell — Frontend Application Logic
 * Integrates with FastAPI backend for dynamic crop comparison,
 * custom cost recalculations, and historical price trend charts.
 */

// Application State
const state = {
  crops: [],
  districts: [],
  currentCrop: "",
  currentDistrict: "",
  currentQuantity: 50,
  comparisonData: null,
  customTransportRates: {},    // mandi_id -> rate
  customOtherCosts: {},        // mandi_id -> rate
  currentEditingMandi: null,
  trendChartInstance: null
};

// DOM Elements Cache
const elements = {
  cropSelect: document.getElementById("crop-select"),
  districtSelect: document.getElementById("district-select"),
  quantityInput: document.getElementById("quantity-input"),
  cropMspHint: document.getElementById("crop-msp-hint"),
  mspVal: document.getElementById("msp-val"),
  compareForm: document.getElementById("compare-form"),
  calculateBtn: document.getElementById("calculate-btn"),
  resetBtn: document.getElementById("reset-btn"),
  presetBtns: document.querySelectorAll(".preset-btn"),
  
  errorBanner: document.getElementById("error-banner"),
  errorTitle: document.getElementById("error-title"),
  errorMessage: document.getElementById("error-message"),
  errorCloseBtn: document.getElementById("error-close-btn"),
  loadingState: document.getElementById("loading-state"),
  emptyState: document.getElementById("empty-state"),
  resultsSection: document.getElementById("results-section"),

  // Best card elements
  bestMandiName: document.getElementById("best-mandi-name"),
  bestMandiLocation: document.getElementById("best-mandi-location"),
  bestDistance: document.getElementById("best-distance"),
  bestNetProceeds: document.getElementById("best-net-proceeds"),
  bestNetRate: document.getElementById("best-net-rate"),
  bestExplanationText: document.getElementById("best-explanation-text"),
  advantageContainer: document.getElementById("advantage-container"),
  advantageAmount: document.getElementById("advantage-amount"),
  advantageSub: document.getElementById("advantage-sub"),

  // Ledger elements
  ledgerQty: document.getElementById("ledger-qty"),
  ledgerGrossCalc: document.getElementById("ledger-gross-calc"),
  ledgerGrossVal: document.getElementById("ledger-gross-val"),
  ledgerTransportCalc: document.getElementById("ledger-transport-calc"),
  ledgerTransportVal: document.getElementById("ledger-transport-val"),
  ledgerOtherCalc: document.getElementById("ledger-other-calc"),
  ledgerOtherVal: document.getElementById("ledger-other-val"),
  ledgerNetVal: document.getElementById("ledger-net-val"),

  // Table elements
  comparisonTableBody: document.getElementById("comparison-table-body"),
  rankedCountBadge: document.getElementById("ranked-count-badge"),

  // Trend chart elements
  trendsCropName: document.getElementById("trends-crop-name"),
  statCurrent: document.getElementById("stat-current"),
  statAvg: document.getElementById("stat-avg"),
  statMomentum: document.getElementById("stat-momentum"),
  trendChartCanvas: document.getElementById("trendChart"),

  // Custom cost modal elements
  costModal: document.getElementById("cost-modal"),
  modalTitle: document.getElementById("modal-title"),
  modalMandiName: document.getElementById("modal-mandi-name"),
  modalMandiId: document.getElementById("modal-mandi-id"),
  customTransportRate: document.getElementById("custom-transport-rate"),
  customHandlingRate: document.getElementById("custom-handling-rate"),
  defaultTransportHint: document.getElementById("default-transport-hint"),
  defaultHandlingHint: document.getElementById("default-handling-hint"),
  modalCloseBtn: document.getElementById("modal-close-btn"),
  modalResetBtn: document.getElementById("modal-reset-btn"),
  customCostForm: document.getElementById("custom-cost-form"),

  // Data status modal elements
  dataStatusBtn: document.getElementById("data-status-btn"),
  dataBadgeText: document.getElementById("data-badge-text"),
  transparencyModal: document.getElementById("transparency-modal"),
  transparencyCloseBtn: document.getElementById("transparency-close-btn"),
  transparencyOkBtn: document.getElementById("transparency-ok-btn"),
  transparencyNoteText: document.getElementById("transparency-note-text"),
  statusCropsCount: document.getElementById("status-crops-count"),
  statusMandisCount: document.getElementById("status-mandis-count"),
  statusRecordsCount: document.getElementById("status-records-count"),
  statusLastUpdate: document.getElementById("status-last-update"),
};

// Currency Formatter Helper (Indian Numbering Style: 1,00,000)
function formatINR(val) {
  if (val === null || val === undefined || isNaN(val)) return "₹0";
  return "₹" + Number(val).toLocaleString("en-IN", {
    maximumFractionDigits: 2,
    minimumFractionDigits: 0
  });
}

// Initialize Application
async function initApp() {
  setupEventListeners();
  await loadCrops();
  await loadDistricts();
  await loadDataStatus();

  // If Wheat and Patiala are present, pre-fill to give an instant demo experience
  if (elements.cropSelect.querySelector('option[value="Wheat"]')) {
    elements.cropSelect.value = "Wheat";
    updateCropMsp();
  }
  if (elements.districtSelect.querySelector('option[value="Patiala"]')) {
    elements.districtSelect.value = "Patiala";
  }

  // Auto calculate initial comparison for smooth hackathon demonstration
  if (elements.cropSelect.value && elements.districtSelect.value) {
    calculateComparison();
  }
}

// Event Listeners Setup
function setupEventListeners() {
  // Preset buttons
  elements.presetBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      elements.presetBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      elements.quantityInput.value = btn.dataset.qty;
    });
  });

  // Quantity input change
  elements.quantityInput.addEventListener("input", () => {
    const val = elements.quantityInput.value;
    elements.presetBtns.forEach(b => {
      if (b.dataset.qty === val) {
        b.classList.add("active");
      } else {
        b.classList.remove("active");
      }
    });
  });

  // Crop change
  elements.cropSelect.addEventListener("change", () => {
    updateCropMsp();
  });

  // Compare Form Submit
  elements.compareForm.addEventListener("submit", (e) => {
    e.preventDefault();
    calculateComparison();
  });

  // Reset Form
  elements.resetBtn.addEventListener("click", () => {
    state.customTransportRates = {};
    state.customOtherCosts = {};
    elements.cropSelect.selectedIndex = 0;
    elements.districtSelect.selectedIndex = 0;
    elements.quantityInput.value = 50;
    elements.presetBtns.forEach(b => b.classList.remove("active"));
    elements.presetBtns[1].classList.add("active");
    elements.resultsSection.classList.add("hidden");
    elements.emptyState.classList.remove("hidden");
    elements.errorBanner.classList.add("hidden");
    elements.cropMspHint.classList.add("hidden");
  });

  // Error Banner Close
  elements.errorCloseBtn.addEventListener("click", () => {
    elements.errorBanner.classList.add("hidden");
  });

  // Cost Modal Handlers
  elements.modalCloseBtn.addEventListener("click", closeCostModal);
  elements.costModal.addEventListener("click", (e) => {
    if (e.target === elements.costModal) closeCostModal();
  });

  elements.customCostForm.addEventListener("submit", (e) => {
    e.preventDefault();
    applyCustomCosts();
  });

  elements.modalResetBtn.addEventListener("click", () => {
    const mandiId = parseInt(elements.modalMandiId.value);
    delete state.customTransportRates[mandiId];
    delete state.customOtherCosts[mandiId];
    closeCostModal();
    calculateComparison();
  });

  // Transparency Modal Handlers
  elements.dataStatusBtn.addEventListener("click", () => {
    elements.transparencyModal.classList.remove("hidden");
  });
  elements.transparencyCloseBtn.addEventListener("click", () => {
    elements.transparencyModal.classList.add("hidden");
  });
  elements.transparencyOkBtn.addEventListener("click", () => {
    elements.transparencyModal.classList.add("hidden");
  });
  elements.transparencyModal.addEventListener("click", (e) => {
    if (e.target === elements.transparencyModal) {
      elements.transparencyModal.classList.add("hidden");
    }
  });
}

// Load Crops from API
async function loadCrops() {
  try {
    const res = await fetch("/crops");
    if (!res.ok) throw new Error("Failed to load crops");
    state.crops = await res.json();

    elements.cropSelect.innerHTML = '<option value="" disabled selected>-- Select Crop (फसल) --</option>';
    state.crops.forEach(c => {
      const opt = document.createElement("option");
      opt.value = c.name;
      opt.textContent = `${c.name} (${c.hindi_name})`;
      opt.dataset.msp = c.msp_price || "";
      elements.cropSelect.appendChild(opt);
    });
  } catch (err) {
    showError("Data Load Error", "Could not load crops list from backend server. Please verify backend is running.");
  }
}

// Load Districts from API
async function loadDistricts() {
  try {
    const res = await fetch("/districts");
    if (!res.ok) throw new Error("Failed to load districts");
    state.districts = await res.json();

    elements.districtSelect.innerHTML = '<option value="" disabled selected>-- Select District (जिला) --</option>';
    state.districts.forEach(d => {
      const opt = document.createElement("option");
      opt.value = d.district;
      opt.textContent = `${d.district} (${d.state})`;
      elements.districtSelect.appendChild(opt);
    });
  } catch (err) {
    showError("Data Load Error", "Could not load districts from backend.");
  }
}

// Load Data Status from API
async function loadDataStatus() {
  try {
    const res = await fetch("/data-status");
    if (!res.ok) return;
    const data = await res.json();
    elements.dataBadgeText.textContent = data.data_mode;
    elements.transparencyNoteText.textContent = data.transparency_note;
    elements.statusCropsCount.textContent = data.total_crops;
    elements.statusMandisCount.textContent = data.total_mandis;
    elements.statusRecordsCount.textContent = data.total_price_records;
    elements.statusLastUpdate.textContent = data.last_data_update;
  } catch (e) {
    console.warn("Data status endpoint unavailable", e);
  }
}

// Update Crop MSP Hint
function updateCropMsp() {
  const selectedCrop = elements.cropSelect.value;
  const cropObj = state.crops.find(c => c.name === selectedCrop);
  if (cropObj && cropObj.msp_price) {
    elements.mspVal.textContent = `₹${cropObj.msp_price.toLocaleString("en-IN")}/quintal (Official Benchmark)`;
    elements.cropMspHint.classList.remove("hidden");
  } else {
    elements.cropMspHint.classList.add("hidden");
  }
}

// Calculate Comparison Core Action
async function calculateComparison() {
  const crop = elements.cropSelect.value;
  const district = elements.districtSelect.value;
  const quantity = parseFloat(elements.quantityInput.value);

  // Validation
  if (!crop) {
    showError("Missing Crop", "Please select a crop to compare.");
    elements.cropSelect.focus();
    return;
  }
  if (!district) {
    showError("Missing District", "Please select your district.");
    elements.districtSelect.focus();
    return;
  }
  if (isNaN(quantity) || quantity <= 0) {
    showError("Invalid Quantity", "Harvest quantity must be greater than 0 quintals.");
    elements.quantityInput.focus();
    return;
  }
  if (quantity > 20000) {
    showError("Quantity Limit", "Maximum supported quantity is 20,000 quintals.");
    return;
  }

  // Clear previous errors
  hideError();
  elements.loadingState.classList.remove("hidden");
  elements.emptyState.classList.add("hidden");
  elements.resultsSection.classList.add("hidden");

  const payload = {
    crop: crop,
    district: district,
    quantity_quintals: quantity,
    custom_transport_rates: Object.keys(state.customTransportRates).length > 0 ? state.customTransportRates : null,
    custom_other_costs_per_qtl: Object.keys(state.customOtherCosts).length > 0 ? state.customOtherCosts : null
  };

  try {
    const res = await fetch("/compare", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      throw new Error(errData.detail || `Server responded with status ${res.status}`);
    }

    const data = await res.json();
    state.comparisonData = data;
    renderResults(data);

    // Fetch and render price trends for selected crop
    loadTrendsChart(crop);

  } catch (err) {
    showError("Calculation Notice", err.message || "Failed to calculate returns. Please try another crop or district.");
    elements.emptyState.classList.remove("hidden");
  } finally {
    elements.loadingState.classList.add("hidden");
  }
}

// Render Comparison Results
function renderResults(data) {
  const best = data.best_mandi;
  const runnerUp = data.runner_up_mandi;

  // 1. Populate Best Recommendation Card
  elements.bestMandiName.textContent = best.mandi_name;
  elements.bestMandiLocation.textContent = `District ${best.district}, ${best.state} • ${best.market_type}`;
  elements.bestDistance.textContent = `${best.distance_km} km away`;
  elements.bestNetProceeds.textContent = formatINR(best.estimated_proceeds);
  elements.bestNetRate.textContent = `Net ${formatINR(best.net_rate_per_quintal)} / quintal`;
  elements.bestExplanationText.textContent = data.why_best_explanation;

  // Advantage vs 2nd place
  if (runnerUp && data.proceeds_advantage > 0) {
    elements.advantageAmount.textContent = `+${formatINR(data.proceeds_advantage)}`;
    elements.advantageSub.textContent = `(+${data.proceeds_advantage_percentage}%) more in hand than 2nd place (${runnerUp.mandi_name})`;
    elements.advantageContainer.classList.remove("hidden");
  } else if (runnerUp && data.proceeds_advantage === 0) {
    elements.advantageAmount.textContent = "Tied Returns";
    elements.advantageSub.textContent = `Equal net proceeds with ${runnerUp.mandi_name}`;
    elements.advantageContainer.classList.remove("hidden");
  } else {
    elements.advantageContainer.classList.add("hidden");
  }

  // 2. Populate Ledger Breakdown for Best Mandi
  elements.ledgerQty.textContent = data.quantity_quintals;
  elements.ledgerGrossCalc.textContent = `${formatINR(best.modal_price)}/qtl × ${data.quantity_quintals} qtl`;
  elements.ledgerGrossVal.textContent = `+${formatINR(best.gross_value)}`;

  elements.ledgerTransportCalc.textContent = `${best.distance_km} km @ ₹${best.cost_breakdown.transport_rate_per_km_qtl.toFixed(2)}/km/qtl`;
  elements.ledgerTransportVal.textContent = `−${formatINR(best.cost_breakdown.transport_cost_total)}`;

  elements.ledgerOtherCalc.textContent = `Labor ₹${best.cost_breakdown.handling_charge_per_qtl}/qtl + Cess ${best.cost_breakdown.mandi_cess_percent}%`;
  elements.ledgerOtherVal.textContent = `−${formatINR(best.cost_breakdown.other_costs_total)}`;

  elements.ledgerNetVal.textContent = `= ${formatINR(best.estimated_proceeds)}`;

  // 3. Populate Comparison Table Rows
  elements.rankedCountBadge.textContent = `${data.ranked_markets.length} Mandis Evaluated`;
  elements.comparisonTableBody.innerHTML = "";

  data.ranked_markets.forEach((m) => {
    const tr = document.createElement("tr");
    if (m.rank === 1) tr.classList.add("winner-row");

    const isCustomTransport = m.cost_breakdown.is_custom_transport;
    const isCustomOther = m.cost_breakdown.is_custom_other;
    const hasCustom = isCustomTransport || isCustomOther;

    const rankClass = m.rank === 1 ? "rank-1" : (m.rank === 2 ? "rank-2" : "");
    const freshnessHtml = m.is_stale
      ? `<span class="freshness-tag stale">⚠️ Stale (${m.price_date})</span>`
      : `<span class="freshness-tag fresh">✓ Fresh (${m.price_date})</span>`;

    tr.innerHTML = `
      <td>
        <span class="rank-badge ${rankClass}">#${m.rank}</span>
      </td>
      <td>
        <span class="cell-mandi-name">${m.mandi_name}</span>
        <span class="cell-mandi-sub">${m.market_type} • ${m.district}</span>
        ${hasCustom ? '<span class="custom-active-indicator">Custom rate active</span>' : ''}
      </td>
      <td class="cell-num">${m.distance_km} km</td>
      <td class="cell-num"><strong>${formatINR(m.modal_price)}</strong> /qtl</td>
      <td class="cell-num" style="color: #b91c1c;">
        −${formatINR(m.cost_breakdown.transport_cost_total)}
        <small style="display:block; color:#6b7280; font-size:0.75rem;">(${formatINR(m.cost_breakdown.transport_cost_per_qtl)}/qtl)</small>
      </td>
      <td class="cell-num" style="color: #b91c1c;">
        −${formatINR(m.cost_breakdown.other_costs_total)}
      </td>
      <td>
        <span class="cell-proceeds">${formatINR(m.estimated_proceeds)}</span>
      </td>
      <td class="cell-num" style="color: #166534; font-weight: 700;">
        ${formatINR(m.net_rate_per_quintal)} /qtl
      </td>
      <td>
        ${freshnessHtml}
        <small style="display:block; color:#6b7280; font-size:0.72rem; margin-top:2px;">${m.source}</small>
      </td>
      <td>
        <button type="button" class="btn-adjust" data-mandi-id="${m.mandi_id}">
          ✏️ Adjust
        </button>
      </td>
    `;

    // Attach click handler for "Adjust Costs"
    const adjustBtn = tr.querySelector(".btn-adjust");
    adjustBtn.addEventListener("click", () => openCostModal(m));

    elements.comparisonTableBody.appendChild(tr);
  });

  // Reveal results
  elements.resultsSection.classList.remove("hidden");
  elements.resultsSection.scrollIntoView({ behavior: "smooth", block: "start" });
}

// Load and Render 30-Day Historical Price Trends
async function loadTrendsChart(crop) {
  try {
    const res = await fetch(`/prices/trends?crop=${encodeURIComponent(crop)}`);
    if (!res.ok) return;
    const trendData = await res.json();

    elements.trendsCropName.textContent = crop;
    elements.statCurrent.textContent = `Current: ${formatINR(trendData.current_price)}`;
    elements.statAvg.textContent = `30-Day Avg: ${formatINR(trendData.average_price)}`;

    // Set momentum pill
    elements.statMomentum.className = "stat-pill";
    if (trendData.trend_direction === "upward") {
      elements.statMomentum.classList.add("momentum-up");
      elements.statMomentum.textContent = `▲ Rising (+${trendData.trend_change_pct}%)`;
    } else if (trendData.trend_direction === "downward") {
      elements.statMomentum.classList.add("momentum-down");
      elements.statMomentum.textContent = `▼ Falling (${trendData.trend_change_pct}%)`;
    } else {
      elements.statMomentum.textContent = `◆ Stable (${trendData.trend_change_pct}%)`;
    }

    renderChart(trendData.trends);
  } catch (err) {
    console.warn("Trends load failed", err);
  }
}

// Render Chart.js Canvas
function renderChart(points) {
  if (!elements.trendChartCanvas) return;
  const ctx = elements.trendChartCanvas.getContext("2d");

  const labels = points.map(p => {
    // Format date MM-DD
    const parts = p.date.split("-");
    return `${parts[1]}/${parts[2]}`;
  });
  const data = points.map(p => p.modal_price);

  if (state.trendChartInstance) {
    state.trendChartInstance.destroy();
  }

  state.trendChartInstance = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [{
        label: "Benchmark Modal Price (₹/Quintal)",
        data: data,
        borderColor: "#1b4332",
        backgroundColor: "rgba(45, 106, 79, 0.08)",
        borderWidth: 2.5,
        pointBackgroundColor: "#2d6a4f",
        pointRadius: 2.5,
        pointHoverRadius: 6,
        fill: true,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: true,
          position: "top",
          labels: { font: { weight: "600", size: 12 } }
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              return ` Modal Price: ₹${context.raw.toLocaleString("en-IN")}/qtl`;
            }
          }
        }
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: { maxTicksLimit: 10, font: { size: 11 } }
        },
        y: {
          grid: { color: "#e5e7eb" },
          ticks: {
            callback: function(value) { return "₹" + value; },
            font: { size: 11 }
          }
        }
      }
    }
  });
}

// Custom Cost Modal Logic
function openCostModal(mandi) {
  state.currentEditingMandi = mandi;
  elements.modalMandiName.textContent = mandi.mandi_name;
  elements.modalMandiId.value = mandi.mandi_id;

  const currentTransportRate = state.customTransportRates[mandi.mandi_id] !== undefined
    ? state.customTransportRates[mandi.mandi_id]
    : mandi.cost_breakdown.transport_rate_per_km_qtl;

  const currentHandlingRate = state.customOtherCosts[mandi.mandi_id] !== undefined
    ? state.customOtherCosts[mandi.mandi_id]
    : mandi.cost_breakdown.handling_charge_per_qtl;

  elements.customTransportRate.value = currentTransportRate;
  elements.customHandlingRate.value = currentHandlingRate;

  elements.defaultTransportHint.textContent = `Standard benchmark: ₹${mandi.cost_breakdown.transport_rate_per_km_qtl.toFixed(2)}/km/qtl`;
  elements.defaultHandlingHint.textContent = `Standard benchmark: ₹${mandi.cost_breakdown.handling_charge_per_qtl.toFixed(2)}/qtl`;

  elements.costModal.classList.remove("hidden");
}

function closeCostModal() {
  elements.costModal.classList.add("hidden");
  state.currentEditingMandi = null;
}

function applyCustomCosts() {
  const mandiId = parseInt(elements.modalMandiId.value);
  const tRate = parseFloat(elements.customTransportRate.value);
  const hRate = parseFloat(elements.customHandlingRate.value);

  if (isNaN(tRate) || tRate < 0) {
    alert("Please enter a valid transport rate (>= 0)");
    return;
  }
  if (isNaN(hRate) || hRate < 0) {
    alert("Please enter a valid handling rate (>= 0)");
    return;
  }

  state.customTransportRates[mandiId] = tRate;
  state.customOtherCosts[mandiId] = hRate;

  closeCostModal();
  calculateComparison();
}

// Error Handling UI Helpers
function showError(title, message) {
  elements.errorTitle.textContent = title;
  elements.errorMessage.textContent = message;
  elements.errorBanner.classList.remove("hidden");
  elements.errorBanner.scrollIntoView({ behavior: "smooth", block: "center" });
}

function hideError() {
  elements.errorBanner.classList.add("hidden");
}

// Bootstrap on DOM Loaded
document.addEventListener("DOMContentLoaded", initApp);
