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

---
transition: fade-out
---

# Project Overview

<div class="flex items-center justify-center h-full">
<div class="text-center">

## Team Members
<div class="flex justify-center gap-8 pt-6 text-2xl">
<div class="p-4 rounded-lg bg-blue-100 dark:bg-blue-900/30"><strong>Ryan</strong></div>
<div class="p-4 rounded-lg bg-green-100 dark:bg-green-900/30"><strong>Leo</strong></div>
<div class="p-4 rounded-lg bg-purple-100 dark:bg-purple-900/30"><strong>Ethan</strong></div>
</div>

<div class="pt-12">

## Primary Objective

<v-clicks>

- 🎯 <strong>Analyze</strong> global stock market trading behaviors
- 📊 <strong>Identify</strong> patterns in company performance  
- 🔍 <strong>Cluster</strong> companies based on trading characteristics
- 💡 <strong>Generate</strong> actionable insights for investors

</v-clicks>

</div>

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

- <strong>Time Range</strong>: 2000-2025 daily stock prices
- <strong>Global Coverage</strong>: Multiple countries and industries
- <strong>Rich Features</strong>: OHLCV data + metadata (country, industry, dividends)

</v-clicks>
</div>

---
layout: center
class: text-center
---

# Research Questions Overview

<div class="grid grid-cols-2 gap-8 pt-8">

<div class="p-6 rounded-xl bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900/20 dark:to-blue-800/20">
<h3 class="text-xl font-bold text-blue-700 dark:text-blue-300 mb-4">Market Analysis</h3>
<ul class="text-left space-y-2 text-sm">
<li>📈 Highest single-day closing price</li>
<li>📊 Average daily trading volumes</li>
<li>🌍 Geographic distribution</li>
</ul>
</div>

<div class="p-6 rounded-xl bg-gradient-to-br from-green-50 to-green-100 dark:from-green-900/20 dark:to-green-800/20">
<h3 class="text-xl font-bold text-green-700 dark:text-green-300 mb-4">Investment Insights</h3>
<ul class="text-left space-y-2 text-sm">
<li>⚡ Stock volatility patterns</li>
<li>💰 Dividend-paying companies</li>
<li>📈 Long-term trends</li>
<li>🎯 Optimal investment windows</li>
</ul>
</div>

</div>

<div class="pt-8">
<p class="text-gray-600 dark:text-gray-300">7 comprehensive research questions analyzed with data-driven insights</p>
</div>

---
layout: center
---

# Q1: Highest Single-Day Closing Price

<div class="flex items-center justify-center h-full">
<div class="max-w-4xl mx-auto">

<div class="p-8 rounded-2xl bg-gradient-to-r from-blue-50 to-indigo-100 dark:from-blue-900/30 dark:to-indigo-900/30 border-l-8 border-blue-500">

<h2 class="text-2xl font-bold text-blue-700 dark:text-blue-300 mb-6 text-center">Which company had the highest single-day closing price?</h2>

<div class="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-lg mb-6">
top_row = df.loc[df["High"].idxmax()]
</div>

<div class="grid grid-cols-2 gap-8">
<div class="text-center">
<div class="text-4xl font-bold text-indigo-600 mb-2">$3,463.07</div>
<div class="text-lg text-gray-700 dark:text-gray-300">Chipotle Mexican Grill</div>
</div>
<div class="text-center">
<div class="text-2xl font-bold text-blue-600 mb-2">June 18, 2024</div>
<div class="text-lg text-gray-700 dark:text-gray-300">Peak Trading Day</div>
</div>
</div>

</div>

</div>
</div>

---
layout: center
---

# Q2: Average Daily Trading Volume

<div class="flex items-center justify-center h-full">
<div class="max-w-4xl mx-auto">

<div class="p-8 rounded-2xl bg-gradient-to-r from-green-50 to-emerald-100 dark:from-green-900/30 dark:to-emerald-900/30 border-l-8 border-green-500">

<h2 class="text-2xl font-bold text-green-700 dark:text-green-300 mb-6 text-center">What is the average daily trading volume for each company?</h2>

<div class="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-lg mb-6">
avg = df.groupby("Brand_Name")["Volume"].mean()
</div>

<div class="grid grid-cols-3 gap-6">
<div class="text-center p-4 bg-white dark:bg-gray-800 rounded-xl shadow-lg">
<div class="text-3xl font-bold text-blue-600 mb-2">376.7M</div>
<div class="text-lg font-semibold">Apple</div>
<div class="text-sm text-gray-600">shares/day</div>
</div>
<div class="text-center p-4 bg-white dark:bg-gray-800 rounded-xl shadow-lg">
<div class="text-3xl font-bold text-orange-600 mb-2">116.5M</div>
<div class="text-lg font-semibold">Amazon</div>
<div class="text-sm text-gray-600">shares/day</div>
</div>
<div class="text-center p-4 bg-white dark:bg-gray-800 rounded-xl shadow-lg">
<div class="text-3xl font-bold text-red-600 mb-2">112.8M</div>
<div class="text-lg font-semibold">Google</div>
<div class="text-sm text-gray-600">shares/day</div>
</div>
</div>

</div>

</div>
</div>

---
layout: center
---

# Q3: Geographic Distribution

<div class="flex items-center justify-center h-full">
<div class="max-w-4xl mx-auto">

<div class="p-8 rounded-2xl bg-gradient-to-r from-purple-50 to-pink-100 dark:from-purple-900/30 dark:to-pink-900/30 border-l-8 border-purple-500">

<h2 class="text-2xl font-bold text-purple-700 dark:text-purple-300 mb-6 text-center">Which countries have the most companies represented?</h2>

<div class="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-lg mb-6">
country_counts = df["Country"].value_counts()
</div>

<div class="grid grid-cols-3 gap-6">
<div class="text-center p-6 bg-white dark:bg-gray-800 rounded-xl shadow-lg">
<div class="text-4xl mb-2">🇺🇸</div>
<div class="text-2xl font-bold text-blue-600">243,606</div>
<div class="text-lg font-semibold">United States</div>
</div>
<div class="text-center p-6 bg-white dark:bg-gray-800 rounded-xl shadow-lg">
<div class="text-4xl mb-2">🇯🇵</div>
<div class="text-2xl font-bold text-red-600">19,403</div>
<div class="text-lg font-semibold">Japan</div>
</div>
<div class="text-center p-6 bg-white dark:bg-gray-800 rounded-xl shadow-lg">
<div class="text-4xl mb-2">🇩🇪</div>
<div class="text-2xl font-bold text-yellow-600">16,225</div>
<div class="text-lg font-semibold">Germany</div>
</div>
</div>

</div>

</div>
</div>

---
layout: center
---

# Q4: Stock Volatility Analysis

<div class="flex items-center justify-center h-full">
<div class="max-w-4xl mx-auto">

<div class="p-8 rounded-2xl bg-gradient-to-r from-orange-50 to-red-100 dark:from-orange-900/30 dark:to-red-900/30 border-l-8 border-orange-500">

<h2 class="text-2xl font-bold text-orange-700 dark:text-orange-300 mb-6 text-center">Which company had the most volatile stock?</h2>

<div class="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-sm mb-6">
df['Volatility (%)'] = (df['High'] - df['Low']) / df['Low'] * 100
max_vol_row = df.loc[df['Volatility (%)'].idxmax()]
</div>

<div class="grid grid-cols-2 gap-8">
<div class="text-center">
<div class="text-5xl font-bold text-red-600 mb-2">784.21%</div>
<div class="text-xl font-semibold">Puma SE</div>
<div class="text-lg text-gray-700 dark:text-gray-300">Daily Volatility</div>
</div>
<div class="text-center">
<div class="text-2xl font-bold text-orange-600 mb-2">June 10, 2019</div>
<div class="text-lg text-gray-700 dark:text-gray-300">Stock Split Event</div>
<div class="text-sm text-gray-600 dark:text-gray-400">(10:1 split)</div>
</div>
</div>

</div>

</div>
</div>

---
layout: center
---

# Q5: Dividend-Paying Companies

<div class="flex items-center justify-center h-full">
<div class="max-w-4xl mx-auto">

<div class="p-8 rounded-2xl bg-gradient-to-r from-indigo-50 to-blue-100 dark:from-indigo-900/30 dark:to-blue-900/30 border-l-8 border-indigo-500">

<h2 class="text-2xl font-bold text-indigo-700 dark:text-indigo-300 mb-6 text-center">Which companies paid dividends in the dataset?</h2>

<div class="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-lg mb-6">
dividend_companies = df[df["Dividends"] > 0]["Brand_Name"].unique()
print(f"Found {len(dividend_companies)} dividend-paying companies")
</div>

<div class="grid grid-cols-2 gap-8">
<div class="text-center">
<div class="text-4xl font-bold text-indigo-600 mb-2">Multiple</div>
<div class="text-lg text-gray-700 dark:text-gray-300">Blue-Chip Companies</div>
<div class="text-sm text-gray-600 dark:text-gray-400">Consistent dividend payments</div>
</div>
<div class="text-center">
<div class="text-2xl font-bold text-blue-600 mb-2">Key Insight</div>
<div class="text-lg text-gray-700 dark:text-gray-300">Mature, Established Firms</div>
<div class="text-sm text-gray-600 dark:text-gray-400">Strong cash flows</div>
</div>
</div>

</div>

</div>
</div>

---
layout: center
background: https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=1920&h=1080&fit=crop
---

# Q6: Greatest Upward Trend

<div class="backdrop-blur-sm bg-white/80 dark:bg-black/60 p-6 rounded-2xl max-w-5xl mx-auto">

<div class="text-center mb-4">
<h2 class="text-2xl font-bold text-gray-800 dark:text-white">Linear Regression Analysis Results</h2>
</div>

<div class="grid grid-cols-2 gap-6 mb-4">

<div class="text-center">
<img src="/q6.png" class="mx-auto max-w-full h-64 object-contain rounded-lg shadow-lg" alt="3M Company Linear Regression Trend"/>
<p class="text-gray-600 dark:text-gray-300 mt-2 text-sm">3M Company Stock Price Trend with Linear Regression Line</p>
</div>

<div class="flex flex-col justify-center">
<div class="p-4 bg-emerald-100 dark:bg-emerald-900/50 rounded-lg mb-4">
<div class="text-left">
<p><strong>Winner:</strong> 3M Company</p>
<p><strong>Increase:</strong> 874.79%</p>
<p><strong>Period:</strong> 2000-2025</p>
<p><strong>Price Growth:</strong> $16.23 → $158.24</p>
</div>
</div>

<div class="bg-gray-900 text-green-400 p-3 rounded text-xs font-mono">
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(x, y)
increase = (end_pred - start_pred) / start_pred * 100
</div>
</div>

</div>

</div>

---
layout: center
---

# Q7: Best 5-Day Investment Windows

<div class="flex items-center justify-center h-full">
<div class="max-w-4xl mx-auto">

<div class="p-8 rounded-2xl bg-gradient-to-r from-violet-50 to-purple-100 dark:from-violet-900/30 dark:to-purple-900/30 border-l-8 border-violet-500">

<h2 class="text-2xl font-bold text-violet-700 dark:text-violet-300 mb-6 text-center">Best 5-day period to invest in each company?</h2>

<div class="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-sm mb-6">
# O(N) sliding window analysis
df['Close_5'] = df.groupby('Brand_Name')['Close'].shift(-4)
df['Pct5'] = (df['Close_5'] - df['Open']) / df['Open'] * 100
best_windows = df.groupby('Brand_Name')['Pct5'].max().sort_values(ascending=False)
</div>

<div class="grid grid-cols-2 gap-6">
<div class="p-4 bg-white dark:bg-gray-800 rounded-xl shadow-lg">
<h3 class="text-lg font-bold text-violet-600 mb-3">Top Performers</h3>
<ul class="text-sm space-y-1">
<li>• Amazon: 64.83% (Apr 2001)</li>
<li>• Zoom: 56.21% (Aug 2020)</li>
<li>• Adobe: 49.72% (Feb 2000)</li>
<li>• Ubisoft: 36.04% (Sep 2024)</li>
</ul>
</div>
<div class="p-4 bg-violet-100 dark:bg-violet-900/30 rounded-xl">
<h3 class="text-lg font-bold text-violet-700 dark:text-violet-300 mb-3">Key Insight</h3>
<p class="text-sm">Best windows often coincide with major market events: dot-com recovery, COVID-19 tech surge, post-earnings surprises.</p>
</div>
</div>

</div>

</div>
</div>

---
layout: center
background: https://images.unsplash.com/photo-1560472354-8b8b5b113b13?w=1920&h=1080&fit=crop
---

# Visualization 1: Apple Stock Candlestick Chart

<div class="backdrop-blur-sm bg-white/90 dark:bg-black/70 p-4 rounded-2xl max-w-5xl mx-auto">

<div class="text-center mb-3">
<h2 class="text-xl font-bold text-gray-800 dark:text-white">Interactive Plotly Candlestick Visualization</h2>
</div>

<div class="text-center mb-3">
<img src="/candlestick.png" class="mx-auto w-full max-w-4xl h-56 object-cover rounded-lg shadow-lg" alt="Apple Stock Candlestick Chart"/>
</div>

<div class="text-center mb-3">
<div class="bg-gray-900 text-green-400 p-2 rounded text-xs font-mono max-w-2xl mx-auto">
fig = go.Figure(data=[go.Candlestick(x=dates, open=open, high=high, low=low, close=close)])
</div>
</div>

<div class="grid grid-cols-4 gap-3 max-w-3xl mx-auto text-center">
<div class="p-2 bg-blue-100 dark:bg-blue-900/30 rounded">
<div class="text-xs font-bold">📊 25 Years</div>
<div class="text-xs">OHLC Data</div>
</div>
<div class="p-2 bg-green-100 dark:bg-green-900/30 rounded">
<div class="text-xs font-bold">📈 $0.79→$213</div>
<div class="text-xs">Price Growth</div>
</div>
<div class="p-2 bg-yellow-100 dark:bg-yellow-900/30 rounded">
<div class="text-xs font-bold">⚡ Events</div>
<div class="text-xs">Market Cycles</div>
</div>
<div class="p-2 bg-purple-100 dark:bg-purple-900/30 rounded">
<div class="text-xs font-bold">💹 Interactive</div>
<div class="text-xs">Zoom & Hover</div>
</div>
</div>

</div>

---
layout: center
background: https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1920&h=1080&fit=crop
---

# Visualization 2: K-means Clustering Results

<div class="backdrop-blur-sm bg-white/85 dark:bg-black/75 p-4 rounded-2xl max-w-6xl mx-auto">

<div class="text-center mb-3">
<h2 class="text-xl font-bold text-gray-800 dark:text-white">Machine Learning Analysis Results</h2>
</div>

<div class="grid grid-cols-3 gap-3 mb-3">
<div class="text-center">
<img src="/elbow.png" class="mx-auto w-full h-32 object-contain rounded-lg shadow" alt="Elbow Method"/>
<p class="text-xs text-gray-600 dark:text-gray-300 mt-1">Elbow Method</p>
</div>
<div class="text-center">
<img src="/cluster.png" class="mx-auto w-full h-32 object-contain rounded-lg shadow" alt="PCA Plot"/>
<p class="text-xs text-gray-600 dark:text-gray-300 mt-1">PCA Clustering</p>
</div>
<div class="text-center">
<img src="/heatmap.png" class="mx-auto w-full h-32 object-contain rounded-lg shadow" alt="Heatmap"/>
<p class="text-xs text-gray-600 dark:text-gray-300 mt-1">Feature Heatmap</p>
</div>
</div>

<div class="grid grid-cols-2 gap-4 max-w-4xl mx-auto">
<div class="text-center p-3 bg-blue-100 dark:bg-blue-900/30 rounded-lg">
<div class="text-lg font-bold text-blue-600">Cluster 0 (31%)</div>
<div class="text-sm">19 Stable Blue-Chip Stocks</div>
<div class="text-xs text-gray-600 mt-1">Lower volume, reduced volatility</div>
</div>
<div class="text-center p-3 bg-green-100 dark:bg-green-900/30 rounded-lg">
<div class="text-lg font-bold text-green-600">Cluster 1 (69%)</div>
<div class="text-sm">42 High-Activity Growth Stocks</div>
<div class="text-xs text-gray-600 mt-1">Higher volume, increased volatility</div>
</div>
</div>

<div class="text-center mt-3">
<div class="inline-block px-3 py-1 bg-yellow-100 dark:bg-yellow-900/30 rounded text-xs">
<strong>PCA Validation:</strong> 72.6% variance explained | <strong>Optimal k=2</strong> clusters identified
</div>
</div>

</div>

---
layout: center
---

# Visualization 3: Cluster Plot with Centers

<div class="max-w-5xl mx-auto">

<div class="text-center mb-4">
<h2 class="text-2xl font-bold">Static Matplotlib Visualization</h2>
</div>

<div class="text-center mb-4">
<img src="/cluster2.png" class="mx-auto w-full max-w-4xl h-64 object-contain rounded-lg shadow-lg" alt="Cluster Centers Plot"/>
<p class="text-center text-sm text-gray-600 dark:text-gray-300 mt-2">Clustering results with centroids marked</p>
</div>

<div class="grid grid-cols-2 gap-6 max-w-4xl mx-auto">
<div class="p-4 bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900/30 dark:to-blue-800/30 rounded-xl">
<h3 class="text-lg font-bold text-blue-700 dark:text-blue-300 mb-2">Conservative Portfolio</h3>
<ul class="text-sm space-y-1">
<li>• 19 companies (31% of dataset)</li>
<li>• Lower average trading volume</li>
<li>• Reduced price volatility</li>
<li>• Stable long-term investment profile</li>
</ul>
</div>
<div class="p-4 bg-gradient-to-br from-green-50 to-green-100 dark:from-green-900/30 dark:to-green-800/30 rounded-xl">
<h3 class="text-lg font-bold text-green-700 dark:text-green-300 mb-2">Growth Portfolio</h3>
<ul class="text-sm space-y-1">
<li>• 42 companies (69% of dataset)</li>
<li>• Higher average trading activity</li>
<li>• Increased price volatility</li>
<li>• Growth-oriented investment profile</li>
</ul>
</div>
</div>

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
- <strong>Python</strong> ecosystem (pandas, scikit-learn, plotly)
- <strong>Statistical analysis</strong> and hypothesis testing
- <strong>Machine learning</strong> clustering algorithms
- <strong>Interactive visualization</strong> with Plotly

</div>

<div>

### Validation Methods
- <strong>Elbow method</strong> for optimal clustering
- <strong>PCA analysis</strong> for dimensionality reduction  
- <strong>Cross-validation</strong> of results
- <strong>Statistical significance</strong> testing

</div>

</div>

---
layout: center
class: text-center
---

# Conclusions & Impact

<div class="text-xl leading-relaxed pt-8">

<v-clicks>

🎯 <strong>Successfully identified</strong> two distinct trading behavior clusters in global stock markets

📊 <strong>Validated financial theory</strong> through data-driven clustering analysis

💼 <strong>Created actionable framework</strong> for investment decision-making and risk management

🔬 <strong>Demonstrated</strong> the power of machine learning in financial market analysis

🚀 <strong>Provided foundation</strong> for future research and business applications

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

- <strong>Statistical methodology</strong> and validation
- <strong>Feature engineering</strong> process
- <strong>Clustering algorithm</strong> parameters
- <strong>Visualization</strong> implementation
- <strong>Business application</strong> frameworks

<div class="pt-8">
<a href="https://github.com/your-repo/world-stock-analysis" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
  View Project Repository
</a>
</div> 