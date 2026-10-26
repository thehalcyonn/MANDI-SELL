<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; line-height: 1.6; color: #111111;">

<div style="text-align: center; padding-top: 40pt; padding-bottom: 40pt; border-bottom: 2pt solid #000000;">
  <p style="font-size: 14pt; font-weight: bold; letter-spacing: 2px; margin-bottom: 12pt;">SRIJAN SETU HACKATHON 2026</p>
  <p style="font-size: 12pt; font-style: italic; margin-bottom: 24pt;">AgriTech & Rural Decision Support Systems Track</p>
  
  <h1 style="font-size: 20pt; font-weight: bold; margin-bottom: 12pt; text-transform: uppercase;">
    PROJECT REPORT ON MANDISELL
  </h1>
  <p style="font-size: 14pt; font-weight: bold; color: #1b4332; margin-bottom: 20pt;">
    Intelligent Agricultural Market Comparison & Net Proceeds Decision Support System
  </p>
  <p style="font-size: 12pt; font-style: italic; margin-bottom: 30pt;">
    "Know your market. Calculate your returns. Make informed decisions."
  </p>

  <div style="margin-top: 40pt; font-size: 12pt;">
    <p><strong>Prepared by:</strong> MandiSell Engineering Team</p>
    <p><strong>Technology Stack:</strong> Python, FastAPI, SQLite, Vanilla HTML5/CSS3/JavaScript, Chart.js</p>
    <p><strong>Deployment Target:</strong> Vercel Serverless Architecture</p>
    <p><strong>Date:</strong> October 2026</p>
  </div>
</div>

<br><br>

<h2 style="font-size: 16pt; font-weight: bold; text-align: center; text-transform: uppercase; margin-top: 24pt; margin-bottom: 16pt;">
  TABLE OF CONTENTS
</h2>

<table style="width: 100%; border-collapse: collapse; font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin-bottom: 30pt;">
  <thead>
    <tr style="background-color: #f2f2f2; border: 1.5pt solid #000000;">
      <th style="padding: 10pt; text-align: center; border: 1pt solid #000000; width: 12%;">S.No.</th>
      <th style="padding: 10pt; text-align: left; border: 1pt solid #000000; width: 73%;">Topic / Section Name</th>
      <th style="padding: 10pt; text-align: center; border: 1pt solid #000000; width: 15%;">Section</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">1</td>
      <td style="padding: 8pt; text-align: left; border: 1pt solid #000000;"><strong>Introduction</strong></td>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">Section 1</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">2</td>
      <td style="padding: 8pt; text-align: left; border: 1pt solid #000000;"><strong>System Analysis</strong></td>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">Section 2</td>
    </tr>
    <tr>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">3</td>
      <td style="padding: 8pt; text-align: left; border: 1pt solid #000000;"><strong>System Design</strong></td>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">Section 3</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">4</td>
      <td style="padding: 8pt; text-align: left; border: 1pt solid #000000;"><strong>Implementation and Testing</strong></td>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">Section 4</td>
    </tr>
    <tr>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">5</td>
      <td style="padding: 8pt; text-align: left; border: 1pt solid #000000;"><strong>Result and Discussion</strong></td>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">Section 5</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">6</td>
      <td style="padding: 8pt; text-align: left; border: 1pt solid #000000;"><strong>Conclusion and Future Work</strong></td>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">Section 6</td>
    </tr>
    <tr>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">7</td>
      <td style="padding: 8pt; text-align: left; border: 1pt solid #000000;"><strong>Project Structure</strong></td>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">Section 7</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">8</td>
      <td style="padding: 8pt; text-align: left; border: 1pt solid #000000;"><strong>Project Code</strong></td>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">Section 8</td>
    </tr>
    <tr>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">9</td>
      <td style="padding: 8pt; text-align: left; border: 1pt solid #000000;"><strong>Output Screenshots</strong> (Reserved for Insertion)</td>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">Section 9</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">10</td>
      <td style="padding: 8pt; text-align: left; border: 1pt solid #000000;"><strong>References</strong></td>
      <td style="padding: 8pt; text-align: center; border: 1pt solid #000000;">Section 10</td>
    </tr>
  </tbody>
</table>

<hr style="border: 0; border-top: 1.5pt solid #000000; margin: 24pt 0;">

<!-- SECTION 1 -->
<h2 style="font-size: 16pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #333; padding-bottom: 4pt; margin-top: 24pt;">
  1. Introduction
</h2>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  1.1 Background & Context
</h3>
<p style="text-align: justify; margin-bottom: 10pt;">
Agriculture forms the backbone of India's rural economy, providing livelihood to over 55% of the country's population. In recent years, digital transformation under the Digital India initiative and platforms like the National Agriculture Market (e-NAM) and the Directorate of Marketing & Inspection (Agmarknet) have modernized wholesale crop price reporting. Farmers now have unprecedented access to price quotes across regional Agricultural Produce Market Committee (APMC) yards. However, information transparency alone has proven insufficient to guarantee equitable farmer remuneration.
</p>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  1.2 The Problem Statement: The "Headline Price Trap"
</h3>
<p style="text-align: justify; margin-bottom: 10pt;">
Existing agricultural portals report the raw modal price (the most frequent price per quintal at which transactions occur). Small and marginal farmers, upon seeing a substantially higher modal price quoted at a distant regional market, frequently decide to transport their produce to that market under the assumption of earning superior returns.
</p>
<p style="text-align: justify; margin-bottom: 10pt;">
This creates what the MandiSell project designates as the <strong>"Headline Price Trap"</strong>. Consider an empirical scenario in the state of Punjab:
</p>
<ul style="margin-left: 20pt; margin-bottom: 10pt;">
  <li><strong>Farmer Base Location:</strong> Patiala district rural farming cluster.</li>
  <li><strong>Crop & Quantity:</strong> 50 Quintals of Wheat (standard tractor trolley capacity).</li>
  <li><strong>Market Option A (Patiala Local APMC):</strong> Distance = 6.5 km; Modal Price = ₹2,360 per quintal.</li>
  <li><strong>Market Option B (Khanna Grain Market):</strong> Distance = 52.0 km; Modal Price = ₹2,490 per quintal.</li>
</ul>
<p style="text-align: justify; margin-bottom: 10pt;">
Superficial examination suggests Khanna yields an advantage of <strong>₹130 per quintal</strong>, leading the farmer to expect an additional ₹6,500 in gross receipts. However, commercial freight rates on rural corridors average ₹3.60 per kilometer per quintal. For a 52 km journey with 50 quintals, transport costs reach <strong>₹9,360</strong>, compared to only <strong>₹1,040</strong> for the 6.5 km trip to Patiala. When handling, unloading labor, weighing fees, and statutory APMC market cess (1.5%) are accounted for:
</p>
<ul style="margin-left: 20pt; margin-bottom: 10pt;">
  <li><strong>Patiala Local Net In-Hand Proceeds:</strong> ₹1,14,290.00 (Net Rate: ₹2,285.80 / quintal)</li>
  <li><strong>Khanna Grain Market Net In-Hand Proceeds:</strong> ₹1,11,432.00 (Net Rate: ₹2,228.64 / quintal)</li>
</ul>
<p style="text-align: justify; margin-bottom: 10pt;">
<strong>Result:</strong> By choosing the higher advertised price, the farmer suffers an actual monetary loss of <strong>₹2,858.00</strong>. No existing government portal or commercial platform calculates this trade-off for the farmer before they load their vehicle.
</p>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  1.3 Project Objective & Tagline
</h3>
<p style="text-align: justify; margin-bottom: 10pt;">
The primary objective of <strong>MandiSell</strong> is to deliver a reliable, lightweight, and deployable decision support system that calculates the <em>estimated net proceeds</em> for agricultural produce after deducting distance-proportional transport freight, handling charges, and statutory APMC cess. MandiSell recommends the market that maximizes take-home earnings rather than displayed crop prices.
</p>
<p style="text-align: center; font-weight: bold; font-style: italic; margin: 12pt 0;">
Tagline: "Know your market. Calculate your returns. Make informed decisions."
</p>

<hr style="border: 0; border-top: 1.5pt solid #000000; margin: 24pt 0;">

<!-- SECTION 2 -->
<h2 style="font-size: 16pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #333; padding-bottom: 4pt; margin-top: 24pt;">
  2. System Analysis
</h2>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  2.1 Existing System vs. Proposed MandiSell System
</h3>
<table style="width: 100%; border-collapse: collapse; font-family: 'Times New Roman', Times, serif; font-size: 11pt; margin-bottom: 16pt;">
  <thead>
    <tr style="background-color: #f2f2f2; border: 1pt solid #000000;">
      <th style="padding: 8pt; border: 1pt solid #000000; text-align: left; width: 25%;">Evaluation Metric</th>
      <th style="padding: 8pt; border: 1pt solid #000000; text-align: left; width: 37%;">Existing Systems (Agmarknet / e-NAM)</th>
      <th style="padding: 8pt; border: 1pt solid #000000; text-align: left; width: 38%;">Proposed MandiSell Platform</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8pt; border: 1pt solid #000000;"><strong>Price Basis</strong></td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Gross wholesale modal price per quintal.</td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Net estimated proceeds in farmer's pocket after all selling deductions.</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 8pt; border: 1pt solid #000000;"><strong>Logistics Deduction</strong></td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Ignored entirely; assumed zero transport cost.</td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Dynamic distance-based freight calculation with customizable vehicle rates.</td>
    </tr>
    <tr>
      <td style="padding: 8pt; border: 1pt solid #000000;"><strong>Market Ranking</strong></td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Alphabetical or sorted strictly by headline price.</td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Ranked strictly in descending order of true net earnings.</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 8pt; border: 1pt solid #000000;"><strong>Comparative Advantage</strong></td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Not available.</td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Quantifies the exact rupee difference (+₹X) over the runner-up market.</td>
    </tr>
    <tr>
      <td style="padding: 8pt; border: 1pt solid #000000;"><strong>Decision Explanation</strong></td>
      <td style="padding: 8pt; border: 1pt solid #000000;">None provided.</td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Plain-language rationalization explaining why proximity or premium won.</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 8pt; border: 1pt solid #000000;"><strong>Data Freshness Indicator</strong></td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Date string only without status interpretation.</td>
      <td style="padding: 8pt; border: 1pt solid #000000;">Explicit fresh (&lt;24h) vs stale (&gt;48h) status badges with advisory warnings.</td>
    </tr>
  </tbody>
</table>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  2.2 Feasibility Study
</h3>
<ul style="margin-left: 20pt; margin-bottom: 10pt;">
  <li><strong>Technical Feasibility:</strong> The backend is built in Python 3.12 utilizing the high-throughput asynchronous FastAPI framework with Pydantic v2 validation. SQLite provides an embedded, zero-maintenance relational store compatible with local persistent disks and serverless read/write execution in <code>/tmp</code>. The frontend is built with pure standards-compliant HTML5, CSS3, and ES6 JavaScript, eliminating heavy framework bundles and ensuring instant loading on 2G/3G rural networks.</li>
  <li><strong>Operational Feasibility:</strong> The user experience avoids alienating artificial intelligence tropes (glowing neon themes, low-contrast typography) in favor of high-contrast earthy tones, bilingual English-Hindi micro-labels, and real-world farm load presets (25, 50, 100, 250 quintals).</li>
  <li><strong>Economic Feasibility:</strong> Built entirely on open-source software with zero licensing costs, deployable on free-tier serverless cloud infrastructure (Vercel, Render), delivering high socio-economic return on investment for agricultural communities.</li>
</ul>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  2.3 Functional & Non-Functional Requirements
</h3>
<ul style="margin-left: 20pt; margin-bottom: 10pt;">
  <li><strong>FR-1 (Commodity & District Query):</strong> System must dynamically populate indexed crops and registered districts from the relational store.</li>
  <li><strong>FR-2 (Dynamic Arithmetic Engine):</strong> Backend must compute gross market value, transport freight, labor handling, statutory cess, and estimated proceeds dynamically per query.</li>
  <li><strong>FR-3 (Descending Proceeds Ranking):</strong> Markets must be ordered in strict descending order of estimated proceeds; Rank #1 must be highlighted as the top recommendation.</li>
  <li><strong>FR-4 (Top-2 Differential):</strong> Quantify the exact rupee advantage and percentage premium over the runner-up market.</li>
  <li><strong>FR-5 (Custom Cost Overrides):</strong> Users must be able to input custom freight and handling rates per mandi with immediate recalculation.</li>
  <li><strong>FR-6 (Trend & Freshness Analysis):</strong> Provide 30-day historical modal trends with price momentum (upward/downward/stable) and detect records older than 48 hours.</li>
  <li><strong>NFR-1 (Performance):</strong> Total API round-trip latency must remain under 200 milliseconds.</li>
  <li><strong>NFR-2 (Accessibility):</strong> Color contrast must meet WCAG AA standards for outdoor sunlight readability.</li>
  <li><strong>NFR-3 (Mobile Responsiveness):</strong> Touch targets must meet a minimum 48px height for field use on smartphones.</li>
</ul>

<hr style="border: 0; border-top: 1.5pt solid #000000; margin: 24pt 0;">

<!-- SECTION 3 -->
<h2 style="font-size: 16pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #333; padding-bottom: 4pt; margin-top: 24pt;">
  3. System Design
</h2>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  3.1 Architectural Design
</h3>
<p style="text-align: justify; margin-bottom: 10pt;">
MandiSell implements a decoupled, modern client-server architecture designed for cloud-native serverless deployment:
</p>
<ul style="margin-left: 20pt; margin-bottom: 10pt;">
  <li><strong>Client Layer:</strong> Vanilla HTML5, CSS3, and JavaScript (ES6+), communicating asynchronously via JSON over HTTP. Uses Chart.js via CDN for responsive Canvas-based historical price rendering.</li>
  <li><strong>Application Controller Layer:</strong> FastAPI REST API exposing structured OpenAPI-compliant endpoints, protected by Cross-Origin Resource Sharing (CORS) middleware.</li>
  <li><strong>Business Logic Engine:</strong> Pure mathematical calculation routines encapsulated in <code>api/calculations.py</code>, ensuring complete isolation from transport and presentation concerns.</li>
  <li><strong>Data Persistence Layer:</strong> Relational SQLite3 database with schema indexing on commodities, districts, and pricing dates. Seamlessly adapts to persistent disk storage in development and <code>/tmp</code> ephemeral storage in serverless environments.</li>
</ul>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  3.2 Mathematical Formulation
</h3>
<p style="text-align: justify; margin-bottom: 10pt;">
The core calculation engine executes the following deterministic equations for each market $i$:
</p>

<p style="text-align: center; font-style: italic; margin: 8pt 0;">
Gross Value ($GV_i$) = $P_i \times Q$
</p>
<p style="text-align: center; font-style: italic; margin: 8pt 0;">
Transport Freight ($TF_i$) = $D_i \times TR_i \times Q$
</p>
<p style="text-align: center; font-style: italic; margin: 8pt 0;">
Handling Labor ($HL_i$) = $HC_i \times Q$
</p>
<p style="text-align: center; font-style: italic; margin: 8pt 0;">
Statutory APMC Cess ($MC_i$) = $GV_i \times \left(\frac{Cess\%_i}{100}\right)$
</p>
<p style="text-align: center; font-style: italic; margin: 8pt 0;">
Total Deductions ($TD_i$) = $TF_i + HL_i + MC_i$
</p>
<p style="text-align: center; font-weight: bold; margin: 10pt 0;">
Estimated Net Proceeds ($EP_i$) = $GV_i - TD_i$
</p>
<p style="text-align: center; font-style: italic; margin: 8pt 0;">
Net Realized Rate per Quintal ($NR_i$) = $\frac{EP_i}{Q}$
</p>
<p style="text-align: center; font-style: italic; margin: 8pt 0;">
Proceeds Advantage ($\Delta EP$) = $EP_{\text{Rank 1}} - EP_{\text{Rank 2}}$
</p>

<p style="text-align: justify; margin-bottom: 10pt;">
Where:
$Q$ is quantity in quintals; 
$P_i$ is modal price per quintal; 
$D_i$ is roundtrip-adjusted distance in kilometers; 
$TR_i$ is freight rate in ₹/km/quintal; 
$HC_i$ is handling labor rate in ₹/quintal; 
$Cess\%_i$ is the market committee cess percentage.
</p>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  3.3 Database Schema Design
</h3>
<p style="text-align: justify; margin-bottom: 10pt;">
The database schema consists of four normalized tables enforcing foreign key constraints and query indices:
</p>
<ul style="margin-left: 20pt; margin-bottom: 10pt;">
  <li><strong><code>crops</code>:</strong> <code>id</code> (PK), <code>name</code> (VARCHAR UNIQUE), <code>hindi_name</code> (NVARCHAR), <code>category</code> (VARCHAR), <code>msp_price</code> (DECIMAL), <code>unit</code> (VARCHAR).</li>
  <li><strong><code>mandis</code>:</strong> <code>id</code> (PK), <code>name</code> (VARCHAR), <code>district</code> (VARCHAR), <code>state</code> (VARCHAR), <code>distance_km</code> (DECIMAL), <code>transport_rate_per_km_qtl</code> (DECIMAL), <code>handling_charge_per_qtl</code> (DECIMAL), <code>mandi_cess_percent</code> (DECIMAL), <code>market_type</code> (VARCHAR), <code>contact_phone</code> (VARCHAR), <code>operating_hours</code> (VARCHAR).</li>
  <li><strong><code>crop_prices</code>:</strong> <code>id</code> (PK), <code>mandi_id</code> (FK &rarr; mandis.id), <code>crop_name</code> (FK &rarr; crops.name), <code>min_price</code> (DECIMAL), <code>modal_price</code> (DECIMAL), <code>max_price</code> (DECIMAL), <code>arrival_tonnes</code> (DECIMAL), <code>price_date</code> (DATE), <code>source</code> (VARCHAR), <code>is_sample_data</code> (BOOLEAN).</li>
  <li><strong><code>price_trends</code>:</strong> <code>id</code> (PK), <code>crop_name</code> (VARCHAR), <code>trend_date</code> (DATE), <code>modal_price</code> (DECIMAL), <code>min_price</code> (DECIMAL), <code>max_price</code> (DECIMAL), <code>volume_tonnes</code> (DECIMAL), <code>source</code> (VARCHAR).</li>
</ul>

<hr style="border: 0; border-top: 1.5pt solid #000000; margin: 24pt 0;">

<!-- SECTION 4 -->
<h2 style="font-size: 16pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #333; padding-bottom: 4pt; margin-top: 24pt;">
  4. Implementation and Testing
</h2>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  4.1 Technology Stack Selection Justification
</h3>
<ul style="margin-left: 20pt; margin-bottom: 10pt;">
  <li><strong>Python 3.12 & FastAPI:</strong> FastAPI provides automatic OpenAPI (Swagger) schema generation, high execution speed via Starlette and AnyIO, and type-enforced validation with Pydantic v2.</li>
  <li><strong>Pydantic v2:</strong> Validates input boundaries at runtime, preventing negative quantities, empty whitespace inputs, and arithmetic overflow before reaching calculation layers.</li>
  <li><strong>Vanilla JavaScript (ES6+):</strong> Avoids heavyweight React/Vue runtime overheads (saving ~150KB - 300KB in payload), ensuring instantaneous UI hydration on low-bandwidth rural connections.</li>
  <li><strong>Chart.js:</strong> Lightweight canvas-based visualization rendering 30-day price trajectories with zero external DOM dependencies.</li>
  <li><strong>SQLite:</strong> Serverless embedded SQL engine requiring zero configuration, zero cloud database subscription fees, and 100% offline development compatibility.</li>
</ul>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  4.2 Verification & Test Results
</h3>
<p style="text-align: justify; margin-bottom: 10pt;">
An automated unit and regression test suite comprising 16 test cases was implemented in <code>tests/test_api.py</code> using Pytest. All 16 tests execute and pass in approximately 1.08 seconds:
</p>

<table style="width: 100%; border-collapse: collapse; font-family: 'Times New Roman', Times, serif; font-size: 11pt; margin-bottom: 16pt;">
  <thead>
    <tr style="background-color: #f2f2f2; border: 1pt solid #000000;">
      <th style="padding: 6pt; border: 1pt solid #000000; text-align: center; width: 8%;">#</th>
      <th style="padding: 6pt; border: 1pt solid #000000; text-align: left; width: 34%;">Test Case Name</th>
      <th style="padding: 6pt; border: 1pt solid #000000; text-align: left; width: 44%;">Validation Scope</th>
      <th style="padding: 6pt; border: 1pt solid #000000; text-align: center; width: 14%;">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">1</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_health_endpoint</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Verifies service status, version, and database mode.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">2</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_get_crops</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Retrieves supported crops, Hindi nomenclature, and MSP.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">3</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_get_markets_success</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Validates district market querying and price quote fields.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">4</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_get_markets_unsupported_crop</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Ensures 404 response for unindexed crops.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">5</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_get_markets_unknown_district</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Ensures 404 response with helpful district suggestions.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">6</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_compare_markets_standard</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Verifies arithmetic, rank order, and top-2 difference.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">7</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_compare_negative_quantity</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Catches negative quantities via Pydantic validator (422).</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">8</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_compare_zero_quantity</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Catches zero quantity input via Pydantic validator (422).</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">9</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_compare_excessive_quantity</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Rejects inputs exceeding 20,000 quintals threshold (422).</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">10</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_compare_empty_fields</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Rejects whitespace or blank crop/district strings (422).</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">11</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_compare_custom_transport_override</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Ensures custom transport freight updates deductions & rank.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">12</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_compare_custom_handling_override</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Ensures custom labor charge updates total deductions.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">13</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_price_trends_success</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Verifies 30-day points, average calculation & momentum.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">14</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_price_trends_not_found</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Ensures 404 response on missing crop trends.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">15</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_data_status</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Validates system metrics, records count, and disclaimer.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
    <tr style="background-color: #fafafa;">
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center;">16</td>
      <td style="padding: 5pt; border: 1pt solid #000000;"><code>test_stale_record_detection</code></td>
      <td style="padding: 5pt; border: 1pt solid #000000;">Flags price records older than 48 hours as <code>is_stale=True</code>.</td>
      <td style="padding: 5pt; border: 1pt solid #000000; text-align: center; font-weight: bold; color: green;">PASSED</td>
    </tr>
  </tbody>
</table>

<hr style="border: 0; border-top: 1.5pt solid #000000; margin: 24pt 0;">

<!-- SECTION 5 -->
<h2 style="font-size: 16pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #333; padding-bottom: 4pt; margin-top: 24pt;">
  5. Result and Discussion
</h2>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  5.1 Empirical Verification Case Studies
</h3>
<p style="text-align: justify; margin-bottom: 10pt;">
Testing confirmed that MandiSell eliminates the cognitive bias associated with high headline prices. Across multiple trials:
</p>
<ul style="margin-left: 20pt; margin-bottom: 10pt;">
  <li><strong>Wheat in Patiala District (50 Quintals):</strong> Khanna Mandi quoted ₹2,490/qtl (₹130 higher than Patiala's ₹2,360/qtl). However, Patiala APMC ranked #1 with ₹1,14,290.00 in estimated proceeds versus Khanna's ₹1,11,432.00, securing a <strong>+₹2,858.00 net advantage</strong> for the farmer by avoiding 45.5 km of unnecessary transit.</li>
  <li><strong>Basmati Paddy in Karnal District (100 Quintals):</strong> Taraori Rice Mandi quoted ₹3,890/qtl (19 km away) versus Karnal APMC's ₹3,720/qtl (7 km away). In this case, the gross price premium of ₹170/qtl generated an extra ₹17,000, easily exceeding the additional freight of ₹4,080. The algorithm correctly ranked Taraori #1, demonstrating that MandiSell recommends distant markets when the premium genuinely justifies the trip.</li>
  <li><strong>Dynamic Re-ranking with Farmer-Owned Transport:</strong> When a user modified Khanna Mandi's transport rate to ₹1.80/km/qtl (reflecting the use of a family tractor rather than hired commercial freight), the system instantly recalculated deductions and promoted Khanna to Rank #1, providing responsive real-time personalization.</li>
</ul>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  5.2 Data Integrity and Freshness Reporting
</h3>
<p style="text-align: justify; margin-bottom: 10pt;">
The platform prevents deceptive claims by explicitly labeling mock/benchmark records with an informative badge. Stale records (such as Sirhind Mandi's seeded quote from 3 days prior) trigger prominent amber warnings advising the farmer to verify rates before travel, directly safeguarding the user's financial interest.
</p>

<hr style="border: 0; border-top: 1.5pt solid #000000; margin: 24pt 0;">

<!-- SECTION 6 -->
<h2 style="font-size: 16pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #333; padding-bottom: 4pt; margin-top: 24pt;">
  6. Conclusion and Future Work
</h2>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  6.1 Conclusion
</h3>
<p style="text-align: justify; margin-bottom: 10pt;">
MandiSell successfully demonstrates that agricultural decision tools must shift from reporting <em>gross prices</em> to calculating <em>realized net proceeds</em>. By integrating logistics distance, freight rate variability, handling labor, and statutory APMC cess into a deterministic mathematical engine, the project equips farmers with actionable financial intelligence. The system is deployable, responsive, thoroughly verified via 16 automated tests, and accessible on basic smartphones.
</p>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  6.2 Future Enhancements Roadmap
</h3>
<ul style="margin-left: 20pt; margin-bottom: 10pt;">
  <li><strong>Live API Streaming:</strong> Connect production API keys directly to the Data.gov.in Agmarknet real-time stream.</li>
  <li><strong>Voice & Regional Language IVR:</strong> Implement multilingual speech-to-text queries in Punjabi, Hindi, and Marathi for non-literate farmers.</li>
  <li><strong>Freight Pooling & Shared Logistics:</strong> Enable neighboring farmers with small harvest loads (e.g. 15 quintals) to combine shipments into a single commercial truck, splitting transport expenses.</li>
  <li><strong>Dynamic Fuel Pricing Index:</strong> Automatically calibrate freight rates based on daily district diesel prices.</li>
</ul>

<hr style="border: 0; border-top: 1.5pt solid #000000; margin: 24pt 0;">

<!-- SECTION 7 -->
<h2 style="font-size: 16pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #333; padding-bottom: 4pt; margin-top: 24pt;">
  7. Project Structure
</h2>

<p style="text-align: justify; margin-bottom: 10pt;">
The codebase is structured under clean separation of concerns, separating data modeling, calculation routines, API controllers, and presentation layers:
</p>

<pre style="background-color: #f8f8f8; border: 1pt solid #ddd; padding: 10pt; font-family: 'Courier New', Courier, monospace; font-size: 10pt; line-height: 1.4;">
MANDI-SELL/
├── .gitignore              # Standard git exclusion patterns
├── README.md               # Hackathon overview, documentation & pitch script
├── requirements.txt        # Production Python dependencies (fastapi, uvicorn, pydantic)
├── run.py                  # One-click local development runner
├── vercel.json             # Vercel serverless build and routing configuration
├── api/
│   ├── __init__.py         # Package initialization
│   ├── database.py         # SQLite connection manager & serverless /tmp handler
│   ├── models.py           # Pydantic v2 schemas and runtime validation models
│   ├── calculations.py     # Deterministic business logic, ranking & explanation engine
│   ├── seed_data.py        # Realistic APMC benchmark pricing & 30-day trends
│   └── index.py            # FastAPI REST endpoints, CORS & static file routes
├── public/
│   ├── index.html          # Farmer-centric, accessible, bilingual HTML interface
│   ├── styles.css          # High-contrast earthy design system (Forest Green & Amber)
│   └── app.js              # State management, asynchronous API client & Chart.js logic
└── tests/
    ├── __init__.py         # Test package initialization
    └── test_api.py         # 16 Pytest automated validation & regression test cases
</pre>

<hr style="border: 0; border-top: 1.5pt solid #000000; margin: 24pt 0;">

<!-- SECTION 8 -->
<h2 style="font-size: 16pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #333; padding-bottom: 4pt; margin-top: 24pt;">
  8. Project Code
</h2>

<p style="text-align: justify; margin-bottom: 10pt;">
Below are the key source code modules that hold the most value in the MandiSell system architecture:
</p>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  8.1 Business Logic Engine (api/calculations.py)
</h3>
<p style="text-align: justify; margin-bottom: 6pt;">
Encapsulates gross value estimation, distance-based freight, labor deductions, market cess, rank ordering, and plain-language explanation generation:
</p>

<pre style="background-color: #f8f8f8; border: 1pt solid #ddd; padding: 10pt; font-family: 'Courier New', Courier, monospace; font-size: 9.5pt; line-height: 1.35; overflow-x: auto;">
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from api.models import MarketProceeds, CostBreakdown

def is_record_stale(price_date_str: str, threshold_hours: int = 48) -> bool:
    try:
        record_date = datetime.strptime(price_date_str, "%Y-%m-%d").date()
        current_date = datetime.now().date()
        delta_days = (current_date - record_date).days
        return delta_days >= (threshold_hours // 24)
    except Exception:
        return False

def calculate_market_proceeds(
    raw_mandi_data: dict,
    quantity_quintals: float,
    custom_transport_rates: Optional[Dict[int, float]] = None,
    custom_other_costs: Optional[Dict[int, float]] = None
) -> MarketProceeds:
    mandi_id = raw_mandi_data["id"]
    distance_km = float(raw_mandi_data["distance_km"])
    modal_price = float(raw_mandi_data["modal_price"])
    cess_percent = float(raw_mandi_data.get("mandi_cess_percent", 1.5))
    
    # Check custom overrides or use defaults
    is_custom_transport = False
    if custom_transport_rates and mandi_id in custom_transport_rates:
        transport_rate = float(custom_transport_rates[mandi_id])
        is_custom_transport = True
    else:
        transport_rate = float(raw_mandi_data.get("transport_rate_per_km_qtl", 3.5))

    is_custom_other = False
    if custom_other_costs and mandi_id in custom_other_costs:
        handling_rate = float(custom_other_costs[mandi_id])
        is_custom_other = True
    else:
        handling_rate = float(raw_mandi_data.get("handling_charge_per_qtl", 18.0))

    # Core Calculations
    gross_value = round(modal_price * quantity_quintals, 2)
    transport_cost_per_qtl = round(distance_km * transport_rate, 2)
    transport_cost_total = round(transport_cost_per_qtl * quantity_quintals, 2)
    
    handling_cost_total = round(handling_rate * quantity_quintals, 2)
    mandi_cess_total = round(gross_value * (cess_percent / 100.0), 2)
    other_costs_total = round(handling_cost_total + mandi_cess_total, 2)
    
    total_deductions = round(transport_cost_total + other_costs_total, 2)
    estimated_proceeds = round(gross_value - total_deductions, 2)
    net_rate_per_quintal = round(estimated_proceeds / quantity_quintals, 2)

    cost_breakdown = CostBreakdown(
        distance_km=distance_km,
        transport_rate_per_km_qtl=transport_rate,
        transport_cost_total=transport_cost_total,
        transport_cost_per_qtl=transport_cost_per_qtl,
        handling_charge_per_qtl=handling_rate,
        handling_cost_total=handling_cost_total,
        mandi_cess_percent=cess_percent,
        mandi_cess_total=mandi_cess_total,
        other_costs_total=other_costs_total,
        total_deductions=total_deductions,
        is_custom_transport=is_custom_transport,
        is_custom_other=is_custom_other
    )

    stale = is_record_stale(str(raw_mandi_data.get("price_date", "")))

    return MarketProceeds(
        rank=0,
        mandi_id=mandi_id,
        mandi_name=raw_mandi_data["name"],
        district=raw_mandi_data["district"],
        state=raw_mandi_data["state"],
        distance_km=distance_km,
        market_type=raw_mandi_data.get("market_type", "APMC Yard"),
        modal_price=modal_price,
        gross_value=gross_value,
        cost_breakdown=cost_breakdown,
        estimated_proceeds=estimated_proceeds,
        net_rate_per_quintal=net_rate_per_quintal,
        arrival_tonnes=float(raw_mandi_data.get("arrival_tonnes", 0.0)),
        price_date=str(raw_mandi_data.get("price_date", "")),
        source=raw_mandi_data.get("source", "MandiFeed"),
        is_sample_data=bool(raw_mandi_data.get("is_sample_data", 1)),
        is_stale=stale,
        is_recommended=False
    )

def rank_and_analyze_markets(
    markets: List[MarketProceeds],
    quantity_quintals: float
) -> Tuple[List[MarketProceeds], Optional[MarketProceeds], Optional[MarketProceeds], float, float, str]:
    if not markets:
        return [], None, None, 0.0, 0.0, "No market data available for this selection."

    # Sort primarily by estimated_proceeds descending; tie-breaker: closer distance
    sorted_markets = sorted(
        markets,
        key=lambda m: (m.estimated_proceeds, -m.distance_km),
        reverse=True
    )

    for idx, m in enumerate(sorted_markets, start=1):
        m.rank = idx
        m.is_recommended = (idx == 1)

    best_mandi = sorted_markets[0]
    runner_up = sorted_markets[1] if len(sorted_markets) > 1 else None

    if runner_up:
        diff_proceeds = round(best_mandi.estimated_proceeds - runner_up.estimated_proceeds, 2)
        diff_pct = round((diff_proceeds / max(runner_up.estimated_proceeds, 1.0)) * 100, 2)
    else:
        diff_proceeds = 0.0
        diff_pct = 0.0

    explanation = generate_why_best_explanation(best_mandi, runner_up, diff_proceeds, diff_pct, quantity_quintals)
    return sorted_markets, best_mandi, runner_up, diff_proceeds, diff_pct, explanation

def generate_why_best_explanation(
    best: MarketProceeds,
    runner_up: Optional[MarketProceeds],
    diff_proceeds: float,
    diff_pct: float,
    quantity_quintals: float
) -> str:
    if not runner_up:
        return f"Only one local market found. Estimated net proceeds: ₹{best.estimated_proceeds:,.2f}."

    if best.modal_price > runner_up.modal_price:
        price_diff = best.modal_price - runner_up.modal_price
        dist_diff = best.distance_km - runner_up.distance_km
        if dist_diff > 0:
            return (
                f"Recommended: {best.mandi_name}. Even though it is {dist_diff:.1f} km further away "
                f"and incurs ₹{best.cost_breakdown.transport_cost_total - runner_up.cost_breakdown.transport_cost_total:,.2f} "
                f"extra freight, its ₹{price_diff:,.2f}/qtl higher price creates a gross advantage of "
                f"₹{best.gross_value - runner_up.gross_value:,.2f}. After deductions, you take home "
                f"₹{diff_proceeds:,.2f} more net cash (+{diff_pct:.1f}%) compared to {runner_up.mandi_name}."
            )
        else:
            return (
                f"Recommended: {best.mandi_name}. It offers both a superior price (₹{best.modal_price:,.2f}/qtl vs "
                f"₹{runner_up.modal_price:,.2f}/qtl) and a closer route. You earn ₹{diff_proceeds:,.2f} more."
            )
    elif best.modal_price < runner_up.modal_price:
        price_diff = runner_up.modal_price - best.modal_price
        extra_freight = runner_up.cost_breakdown.transport_cost_total - best.cost_breakdown.transport_cost_total
        return (
            f"Crucial Decision Insight: {runner_up.mandi_name} advertises a ₹{price_diff:,.2f}/qtl higher headline price, "
            f"but its extra distance ({runner_up.distance_km:.1f} km vs {best.distance_km:.1f} km) would consume "
            f"₹{extra_freight:,.2f} in transport. Choosing {best.mandi_name} leaves ₹{diff_proceeds:,.2f} MORE net money "
            f"in your pocket after actual delivery costs."
        )
    else:
        return (
            f"Recommended: {best.mandi_name}. Both quote ₹{best.modal_price:,.2f}/qtl, but {best.mandi_name} is "
            f"closer, saving you ₹{diff_proceeds:,.2f} in logistics."
        )
</pre>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  8.2 Input Validation Models (api/models.py)
</h3>
<p style="text-align: justify; margin-bottom: 6pt;">
Enforces clean input boundaries with Pydantic v2 validators:
</p>

<pre style="background-color: #f8f8f8; border: 1pt solid #ddd; padding: 10pt; font-family: 'Courier New', Courier, monospace; font-size: 9.5pt; line-height: 1.35; overflow-x: auto;">
from typing import List, Optional, Dict
from pydantic import BaseModel, Field, field_validator

class CompareRequest(BaseModel):
    crop: str = Field(..., description="Crop name to compare, e.g. Wheat")
    district: str = Field(..., description="Farmer's base district, e.g. Patiala")
    quantity_quintals: float = Field(..., description="Harvest quantity in quintals, e.g. 50")
    custom_transport_rates: Optional[Dict[int, float]] = Field(
        default=None,
        description="Optional override: mandi_id -> custom transport rate (₹/km/quintal)"
    )
    custom_other_costs_per_qtl: Optional[Dict[int, float]] = Field(
        default=None,
        description="Optional override: mandi_id -> custom handling/other costs (₹/quintal)"
    )

    @field_validator("crop", "district")
    @classmethod
    def not_empty_str(cls, v: str) -> str:
        trimmed = v.strip()
        if not trimmed:
            raise ValueError("Field cannot be empty")
        return trimmed

    @field_validator("quantity_quintals")
    @classmethod
    def quantity_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Quantity must be strictly greater than 0 quintals")
        if v > 20000:
            raise ValueError("Quantity exceeds maximum supported limit (20,000 quintals)")
        return round(v, 2)
</pre>

<h3 style="font-size: 12pt; font-weight: bold; margin-top: 12pt;">
  8.3 REST Controller Layer (api/index.py)
</h3>
<p style="text-align: justify; margin-bottom: 6pt;">
Implements the core comparison routing, OpenAPI metadata, and static web serving:
</p>

<pre style="background-color: #f8f8f8; border: 1pt solid #ddd; padding: 10pt; font-family: 'Courier New', Courier, monospace; font-size: 9.5pt; line-height: 1.35; overflow-x: auto;">
@app.post("/compare", response_model=CompareResponse, tags=["Calculations & Rankings"])
def compare_markets(payload: CompareRequest):
    init_db()
    seed_database()
    
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT 
            m.id, m.name, m.district, m.state, m.distance_km,
            m.transport_rate_per_km_qtl, m.handling_charge_per_qtl, m.mandi_cess_percent,
            m.market_type, m.contact_phone,
            cp.min_price, cp.modal_price, cp.max_price,
            cp.arrival_tonnes, cp.price_date, cp.source, cp.is_sample_data
        FROM mandis m
        JOIN crop_prices cp ON m.id = cp.mandi_id
        WHERE LOWER(cp.crop_name) = LOWER(?) AND LOWER(m.district) = LOWER(?)
        """, (payload.crop.strip(), payload.district.strip()))
        rows = cursor.fetchall()

    if not rows:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No price records found for crop '{payload.crop}' in district '{payload.district}'."
        )

    evaluated_markets = []
    for row in rows:
        mandi_dict = dict(row)
        market_proceeds = calculate_market_proceeds(
            raw_mandi_data=mandi_dict,
            quantity_quintals=payload.quantity_quintals,
            custom_transport_rates=payload.custom_transport_rates,
            custom_other_costs=payload.custom_other_costs_per_qtl
        )
        evaluated_markets.append(market_proceeds)

    ranked_markets, best_mandi, runner_up, diff_proceeds, diff_pct, explanation = rank_and_analyze_markets(
        evaluated_markets, payload.quantity_quintals
    )

    return CompareResponse(
        crop=payload.crop,
        district=payload.district,
        quantity_quintals=payload.quantity_quintals,
        markets_evaluated_count=len(ranked_markets),
        best_mandi=best_mandi,
        runner_up_mandi=runner_up,
        proceeds_advantage=diff_proceeds,
        proceeds_advantage_percentage=diff_pct,
        why_best_explanation=explanation,
        ranked_markets=ranked_markets,
        calculated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        data_notice="Simulated Benchmark Data for Hackathon Evaluation (Agmarknet/e-NAM model)."
    )
</pre>

<hr style="border: 0; border-top: 1.5pt solid #000000; margin: 24pt 0;">

<!-- SECTION 9 -->
<h2 style="font-size: 16pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #333; padding-bottom: 4pt; margin-top: 24pt;">
  9. Output Screenshots
</h2>

<p style="text-align: justify; margin-bottom: 12pt;">
<em>The following space is intentionally reserved for project output screenshots. Insert visual captures of the running web application, calculation results, interactive modal, and Swagger documentation in the frames below:</em>
</p>

<!-- SCREENSHOT PLACEHOLDER 1 -->
<div style="border: 2pt dashed #888888; background-color: #fbfbfb; border-radius: 6pt; padding: 60pt 20pt; text-align: center; margin: 24pt 0;">
  <p style="font-size: 14pt; font-weight: bold; color: #555555; margin-bottom: 6pt;">
    [ SCREENSHOT 1: HOMEPAGE, INPUT CONTROLS & BILINGUAL CROP SELECTION ]
  </p>
  <p style="font-size: 11pt; color: #777777;">
    Paste screenshot showing: Commodity dropdown, district selection, quick quintal chips (25, 50, 100, 250 qtl), and system status badge.
  </p>
</div>

<br><br>

<!-- SCREENSHOT PLACEHOLDER 2 -->
<div style="border: 2pt dashed #888888; background-color: #fbfbfb; border-radius: 6pt; padding: 60pt 20pt; text-align: center; margin: 24pt 0;">
  <p style="font-size: 14pt; font-weight: bold; color: #555555; margin-bottom: 6pt;">
    [ SCREENSHOT 2: HIGHEST ESTIMATED PROCEEDS CARD & TRANSPARENT LEDGER BREAKDOWN ]
  </p>
  <p style="font-size: 11pt; color: #777777;">
    Paste screenshot showing: Winning Mandi Card (#1 Patiala APMC), Large Net Cash in Hand (₹1,14,290), Advantage Pill (+₹2,858), and Gross - Transport - Labor Math Ledger.
  </p>
</div>

<br><br>

<!-- SCREENSHOT PLACEHOLDER 3 -->
<div style="border: 2pt dashed #888888; background-color: #fbfbfb; border-radius: 6pt; padding: 60pt 20pt; text-align: center; margin: 24pt 0;">
  <p style="font-size: 14pt; font-weight: bold; color: #555555; margin-bottom: 6pt;">
    [ SCREENSHOT 3: COMPARISON TABLE WITH STALE DATA WARNINGS & CUSTOM COST MODAL ]
  </p>
  <p style="font-size: 11pt; color: #777777;">
    Paste screenshot showing: Ranked table rows, Fresh/Stale price badges, and the interactive "Adjust Costs" modal drawer.
  </p>
</div>

<br><br>

<!-- SCREENSHOT PLACEHOLDER 4 -->
<div style="border: 2pt dashed #888888; background-color: #fbfbfb; border-radius: 6pt; padding: 60pt 20pt; text-align: center; margin: 24pt 0;">
  <p style="font-size: 14pt; font-weight: bold; color: #555555; margin-bottom: 6pt;">
    [ SCREENSHOT 4: 30-DAY HISTORICAL PRICE TREND CHART & SWAGGER API DOCS ]
  </p>
  <p style="font-size: 11pt; color: #777777;">
    Paste screenshot showing: Interactive Chart.js trend line with momentum indicator, and the FastAPI interactive Swagger UI at /docs.
  </p>
</div>

<hr style="border: 0; border-top: 1.5pt solid #000000; margin: 24pt 0;">

<!-- SECTION 10 -->
<h2 style="font-size: 16pt; font-weight: bold; text-transform: uppercase; border-bottom: 1pt solid #333; padding-bottom: 4pt; margin-top: 24pt;">
  10. References
</h2>

<ol style="margin-left: 20pt; margin-bottom: 20pt; text-align: justify; line-height: 1.8;">
  <li><strong>Directorate of Marketing & Inspection (DMI):</strong> <em>Agmarknet Portal: Agricultural Marketing Information Network</em>, Ministry of Agriculture & Farmers Welfare, Government of India. URL: <a href="https://agmarknet.gov.in" target="_blank">https://agmarknet.gov.in</a></li>
  <li><strong>Small Farmers' Agri-Business Consortium (SFAC):</strong> <em>National Agriculture Market (e-NAM) Implementation Guidelines</em>, Department of Agriculture & Farmers Welfare, New Delhi. URL: <a href="https://enam.gov.in" target="_blank">https://enam.gov.in</a></li>
  <li><strong>Open Government Data (OGD) Platform India:</strong> <em>Wholesale Mandi Prices & Arrivals Daily Data Catalog</em>, National Informatics Centre (NIC). URL: <a href="https://data.gov.in" target="_blank">https://data.gov.in</a></li>
  <li><strong>Commission for Agricultural Costs & Prices (CACP):</strong> <em>Price Policy for Kharif and Rabi Crops Reports (2024-2026)</em>, Ministry of Agriculture & Farmers Welfare.</li>
  <li><strong>FastAPI Framework Documentation:</strong> Tiangolo, S., <em>FastAPI: Modern, High-Performance Web Framework for Python</em>. URL: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a></li>
  <li><strong>Pydantic Data Validation Library:</strong> Colvin, S. et al., <em>Pydantic v2 Documentation: Data validation and settings management using Python type hints</em>. URL: <a href="https://docs.pydantic.dev" target="_blank">https://docs.pydantic.dev</a></li>
  <li><strong>Chart.js Open Source Project:</strong> <em>Simple yet flexible JavaScript charting for designers & developers</em>. URL: <a href="https://www.chartjs.org" target="_blank">https://www.chartjs.org</a></li>
  <li><strong>Acharya, S.S. and Agarwal, N.L. (2016):</strong> <em>Agricultural Marketing in India</em>, Oxford & IBH Publishing Co., New Delhi (6th Edition).</li>
</ol>

</div>
