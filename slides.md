---
theme: seriph
title: World Stock Price Analysis
subtitle: A Data-Driven Exploration of Global Financial Markets
background: https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1920&h=1080&fit=crop
class: text-center
highlighter: shiki
drawings:
  enabled: true
transition: slide-left
mdc: true
download: true
---

# World Stock Price Analysis
## A Data-Driven Exploration of Global Financial Markets

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

---
transition: fade-out
---

# Team & Objective

<div class="grid grid-cols-2 gap-10 pt-4 -mb-6">

<div>

## Team Members
- **Ryan**
- **Leo** 
- **Ethan**

## Project Duration
**2 weeks** - Comprehensive analysis from data acquisition to presentation

</div>

<div>

## Primary Objective

<v-clicks>

- 🎯 **Analyze** global stock market trading behaviors
- 📊 **Identify** patterns in company performance
- 🔍 **Cluster** companies based on trading characteristics  
- 💡 **Generate** actionable insights for investors

</v-clicks>

</div>

</div>

---
layout: center
class: text-center
---

# Dataset Overview

<div class="grid grid-cols-3 gap-8 pt-8">

<div class="text-center">
<div class="text-6xl text-blue-600 font-bold">310K+</div>
<div class="text-lg text-gray-600">Data Points</div>
</div>

<div class="text-center">
<div class="text-6xl text-green-600 font-bold">62</div>
<div class="text-lg text-gray-600">Companies</div>
</div>

<div class="text-center">
<div class="text-6xl text-purple-600 font-bold">25</div>
<div class="text-lg text-gray-600">Years of Data</div>
</div>

</div>

<div class="pt-8">
<v-clicks>

- **Time Range**: 2000-2025 daily stock prices
- **Global Coverage**: Multiple countries and industries
- **Rich Features**: OHLCV data + metadata (country, industry, dividends)

</v-clicks>
</div>

---
transition: slide-up
---

# Research Questions Investigated

<div class="grid grid-cols-2 gap-6 pt-4">

<div>

## Market Performance 📈
<v-clicks>

1. **Which company had the highest single-day closing price?**
2. **What is the average daily trading volume for each company?**
3. **Which company had the most volatile stock?** (daily range analysis)

</v-clicks>

</div>

<div>

## Trading Patterns 🔄
<v-clicks>

4. **Which countries have the most companies represented?**
5. **Which company's stock showed the greatest upward trend?**
6. **What are the best 5-day investment windows?** (sliding window analysis)
7. **How do companies cluster by trading behavior?** (K-means analysis)

</v-clicks>

</div>

</div>

<style>
.slidev-vclick-target {
  transition: all 500ms ease;
}
</style>

---
layout: image-right
image: https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&h=600&fit=crop
---

# Visualization #1: Candlestick Analysis

## Apple Stock Performance

<v-clicks>

- **Interactive candlestick charts** showing OHLC data
- **Time series analysis** from 2000-2025
- **Price action patterns** and trend identification
- **Volume correlation** with price movements

</v-clicks>

<div class="pt-8">
<v-click>

### Key Insights
- Clear visualization of **bull and bear markets**
- **Volatility clusters** during major events
- **Long-term growth trend** despite short-term fluctuations

</v-click>
</div>

---
layout: center
---

# Visualization #2: K-means Clustering

<div class="grid grid-cols-2 gap-8">

<div>

## Methodology
<v-clicks>

- **6 key features** analyzed:
  - Average trading volume
  - Daily return & volatility  
  - Price volatility
  - Average stock price
  - Volatility score

- **Elbow method** for optimal k=2
- **PCA dimensionality** reduction
- **72.6% variance** explained

</v-clicks>

</div>

<div>

## Cluster Results
<v-clicks>

### Cluster 0: "Stable Blue-Chips" (31%)
- Lower trading volume
- Lower volatility
- Conservative investment profile

### Cluster 1: "High-Activity Growth" (69%) 
- Higher trading volume
- Higher volatility  
- Growth-oriented profile

</v-clicks>

</div>

</div>

---
transition: slide-left
---

# Clustering Insights & Business Applications

<div class="grid grid-cols-2 gap-8 pt-4">

<div>

## Key Findings 🔍

<v-clicks>

- **Market Dichotomy**: Clear separation into conservative vs. growth stocks
- **Risk-Return Validation**: Confirms fundamental finance principles
- **Portfolio Guidance**: Natural framework for asset allocation
- **Statistical Significance**: Strong PCA validation (72.6% variance)

</v-clicks>

</div>

<div>

## Practical Applications 💼

<v-clicks>

**For Asset Managers:**
- Client portfolio recommendations
- Risk assessment frameworks

**For Individual Investors:**  
- Risk tolerance matching
- Strategic asset allocation

**For Analysts:**
- Market segmentation
- Sector rotation strategies

</v-clicks>

</div>

</div>

---
layout: image-left
image: https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop
---

# Visualization #3: Linear Regression Analysis

## Stock Performance Trends

<v-clicks>

- **Trend analysis** for greatest upward movement
- **Statistical significance** testing
- **Performance ranking** across companies
- **Time-based correlation** patterns

</v-clicks>

<div class="pt-8">
<v-click>

### Methodology
- **Linear regression** modeling of price trends
- **R-squared analysis** for trend strength
- **Slope coefficient** comparison
- **Residual analysis** for model validation

</v-click>
</div>

---
layout: center
class: text-center
---

# Key Discoveries & Impact

<div class="grid grid-cols-3 gap-6 pt-8">

<div class="p-6 rounded-lg bg-blue-50 dark:bg-blue-900/20">
<div class="text-3xl mb-4">🎯</div>
<h3 class="text-lg font-bold mb-2">Market Structure</h3>
<p class="text-sm">69-31 split reveals growth-dominated market with clear behavioral patterns</p>
</div>

<div class="p-6 rounded-lg bg-green-50 dark:bg-green-900/20">
<div class="text-3xl mb-4">⚖️</div>
<h3 class="text-lg font-bold mb-2">Risk-Return Trade-off</h3>
<p class="text-sm">Clustering validates fundamental finance principles in real market data</p>
</div>

<div class="p-6 rounded-lg bg-purple-50 dark:bg-purple-900/20">
<div class="text-3xl mb-4">💡</div>
<h3 class="text-lg font-bold mb-2">Investment Framework</h3>
<p class="text-sm">Actionable insights for portfolio construction and strategy development</p>
</div>

</div>

---
layout: center
---

# Methodology & Technical Excellence

<div class="pt-4">

## Data Science Pipeline

```mermaid
graph LR
    A["Data Collection<br/>310K+ records"] --> B["Preprocessing<br/>Feature Engineering"]
    B --> C["Exploratory Analysis<br/>Statistical Testing"]
    C --> D["Machine Learning<br/>K-means Clustering"]
    D --> E["Visualization<br/>Interactive Charts"]
    E --> F["Business Insights<br/>Recommendations"]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#f1f8e9
```

</div>

<div class="grid grid-cols-2 gap-8 pt-8">

<div>

### Technical Stack
- **Python** ecosystem (pandas, scikit-learn, plotly)
- **Statistical analysis** and hypothesis testing
- **Machine learning** clustering algorithms
- **Interactive visualization** with Plotly

</div>

<div>

### Validation Methods
- **Elbow method** for optimal clustering
- **PCA analysis** for dimensionality reduction  
- **Cross-validation** of results
- **Statistical significance** testing

</div>

</div>

---
layout: two-cols
---

# Challenges & Solutions

## Data Challenges
<v-clicks>

- **Large dataset** (310K+ records)
  - *Solution*: Efficient pandas operations
- **Missing values** and data quality
  - *Solution*: Robust preprocessing pipeline
- **Feature engineering** complexity
  - *Solution*: Domain expertise integration

</v-clicks>

## Technical Challenges
<v-clicks>

- **Clustering optimization**
  - *Solution*: Multiple validation methods
- **Visualization performance**
  - *Solution*: Interactive Plotly charts
- **Interpretability**
  - *Solution*: Business-focused analysis

</v-clicks>

::right::

# Future Directions

## Enhanced Analysis
<v-clicks>

- **Real-time data** integration
- **Sentiment analysis** from news/social media
- **Sector-specific** clustering models
- **Time-series forecasting**

</v-clicks>

## Business Applications
<v-clicks>

- **Robo-advisor** integration
- **Risk management** tools
- **ESG factor** incorporation
- **Alternative data** sources

</v-clicks>

---
layout: center
class: text-center
---

# Conclusions & Impact

<div class="text-xl leading-relaxed pt-8">

<v-clicks>

🎯 **Successfully identified** two distinct trading behavior clusters in global stock markets

📊 **Validated financial theory** through data-driven clustering analysis

💼 **Created actionable framework** for investment decision-making and risk management

🔬 **Demonstrated** the power of machine learning in financial market analysis

🚀 **Provided foundation** for future research and business applications

</v-clicks>

</div>

<div class="pt-12">
<v-click>

## Thank You
### Questions & Discussion

</v-click>
</div>

---
layout: center
class: text-center
---

# Appendix: Technical Details

Available for detailed discussion:

- **Statistical methodology** and validation
- **Feature engineering** process
- **Clustering algorithm** parameters
- **Visualization** implementation
- **Business application** frameworks

<div class="pt-8">
<a href="https://github.com/your-repo/world-stock-analysis" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
  View Project Repository
</a>
</div> 