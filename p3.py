import React, { useState, useMemo } from 'react';
import { Slider } from '@/components/ui/slider';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ScatterChart, Scatter } from 'recharts';

// Email: 23f1002246@ds.study.iitm.ac.in

const InteractiveNotebook = () => {
  // Cell 1: Interactive slider widget for sample size
  // This controls how many data points we generate
  const [sampleSize, setSampleSize] = useState(50);
  
  // Cell 2: Generate synthetic dataset based on sample size
  // Data flow: sampleSize -> rawData
  // This cell depends on the slider value from Cell 1
  const rawData = useMemo(() => {
    const data = [];
    for (let i = 0; i < sampleSize; i++) {
      const x = (i / sampleSize) * 10;
      // y = 2x + 3 + noise (linear relationship with random variation)
      const y = 2 * x + 3 + (Math.random() - 0.5) * 2;
      data.push({ 
        x: parseFloat(x.toFixed(2)), 
        y: parseFloat(y.toFixed(2)) 
      });
    }
    return data;
  }, [sampleSize]);
  
  // Cell 3: Calculate statistical measures from the dataset
  // Data flow: rawData -> statistics
  // This cell depends on the generated data from Cell 2
  const statistics = useMemo(() => {
    const xValues = rawData.map(d => d.x);
    const yValues = rawData.map(d => d.y);
    
    const meanX = xValues.reduce((a, b) => a + b, 0) / rawData.length;
    const meanY = yValues.reduce((a, b) => a + b, 0) / rawData.length;
    
    // Calculate correlation coefficient
    let numerator = 0;
    let denomX = 0;
    let denomY = 0;
    
    for (let i = 0; i < rawData.length; i++) {
      const dx = xValues[i] - meanX;
      const dy = yValues[i] - meanY;
      numerator += dx * dy;
      denomX += dx * dx;
      denomY += dy * dy;
    }
    
    const correlation = numerator / Math.sqrt(denomX * denomY);
    
    return {
      meanX: meanX.toFixed(2),
      meanY: meanY.toFixed(2),
      correlation: correlation.toFixed(3),
      minY: Math.min(...yValues).toFixed(2),
      maxY: Math.max(...yValues).toFixed(2)
    };
  }, [rawData]);

  // Cell 4: Dynamic markdown content based on state
  // Data flow: sampleSize, statistics -> dynamicContent
  const dynamicContent = useMemo(() => {
    const corr = parseFloat(statistics.correlation);
    
    let sizeCategory, sizeAdvice;
    if (sampleSize < 50) {
      sizeCategory = '⚠️ Small Sample Analysis';
      sizeAdvice = 'Sample size is relatively small. Consider increasing to at least 50 points for more reliable statistical inference.';
    } else if (sampleSize < 100) {
      sizeCategory = '✓ Medium Sample Analysis';
      sizeAdvice = 'Sample size is adequate for basic statistical analysis.';
    } else {
      sizeCategory = '✓ Large Sample Analysis';
      sizeAdvice = 'Sample size is robust and suitable for reliable statistical inference.';
    }
    
    let corrStrength;
    if (corr > 0.9) corrStrength = 'very strong';
    else if (corr > 0.7) corrStrength = 'strong';
    else if (corr > 0.5) corrStrength = 'moderate';
    else corrStrength = 'weak';
    
    return { sizeCategory, sizeAdvice, corrStrength };
  }, [sampleSize, statistics]);

  return (
    <div className="w-full max-w-6xl mx-auto p-6 space-y-6 bg-gradient-to-br from-slate-50 to-blue-50 min-h-screen">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-slate-800 mb-2">
          Interactive Data Analysis Notebook
        </h1>
        <p className="text-slate-600">Demonstrating variable dependencies and reactive computation</p>
        <p className="text-sm text-slate-500 mt-2">Email: 23f1002246@ds.study.iitm.ac.in</p>
      </div>

      {/* Cell 1: Interactive Slider Widget */}
      <Card className="border-2 border-blue-200 shadow-lg">
        <CardHeader className="bg-blue-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-blue-500 text-white px-3 py-1 rounded text-sm font-mono">Cell 1</span>
            Interactive Slider Widget
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <label className="text-lg font-medium text-slate-700">
                Sample Size: <span className="text-blue-600 font-bold text-2xl">{sampleSize}</span>
              </label>
            </div>
            <Slider
              value={[sampleSize]}
              onValueChange={(value) => setSampleSize(value[0])}
              min={10}
              max={200}
              step={10}
              className="w-full"
            />
            <div className="bg-blue-50 border-l-4 border-blue-500 p-4">
              <p className="text-sm text-slate-700">
                <strong>📍 Variable:</strong> <code className="bg-slate-200 px-2 py-1 rounded font-mono">sampleSize</code>
              </p>
              <p className="text-sm text-slate-600 mt-2">
                💡 This slider controls the number of data points generated. Changes here cascade to all dependent cells below.
              </p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Cell 2: Data Visualization */}
      <Card className="border-2 border-green-200 shadow-lg">
        <CardHeader className="bg-green-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-green-500 text-white px-3 py-1 rounded text-sm font-mono">Cell 2</span>
            Scatter Plot Visualization
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <ResponsiveContainer width="100%" height={350}>
            <ScatterChart margin={{ top: 20, right: 30, bottom: 20, left: 20 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
              <XAxis 
                dataKey="x" 
                name="X Variable" 
                label={{ value: 'X Variable', position: 'insideBottom', offset: -10 }}
                stroke="#64748b"
              />
              <YAxis 
                dataKey="y" 
                name="Y Variable" 
                label={{ value: 'Y Variable', angle: -90, position: 'insideLeft' }}
                stroke="#64748b"
              />
              <Tooltip 
                cursor={{ strokeDasharray: '3 3' }}
                contentStyle={{ backgroundColor: '#f8fafc', border: '1px solid #cbd5e1' }}
              />
              <Legend />
              <Scatter 
                name={`Data Points (n=${sampleSize})`} 
                data={rawData} 
                fill="#3b82f6" 
                fillOpacity={0.6}
              />
            </ScatterChart>
          </ResponsiveContainer>
          <div className="bg-green-50 border-l-4 border-green-500 p-4 mt-4">
            <p className="text-sm text-slate-700">
              <strong>📍 Variable:</strong> <code className="bg-slate-200 px-2 py-1 rounded font-mono">rawData</code>
            </p>
            <p className="text-sm text-slate-600 mt-2">
              <strong>Dependencies:</strong> Depends on <code className="bg-slate-200 px-2 py-1 rounded font-mono">sampleSize</code> from Cell 1
            </p>
            <p className="text-sm text-slate-600 mt-1">
              <strong>Relationship:</strong> <code className="bg-slate-200 px-2 py-1 rounded font-mono">y = 2x + 3 + noise</code>
            </p>
          </div>
        </CardContent>
      </Card>

      {/* Cell 3: Statistical Summary */}
      <Card className="border-2 border-purple-200 shadow-lg">
        <CardHeader className="bg-purple-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-purple-500 text-white px-3 py-1 rounded text-sm font-mono">Cell 3</span>
            Statistical Summary
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mb-4">
            <div className="bg-gradient-to-br from-blue-100 to-blue-50 p-4 rounded-lg border border-blue-200">
              <p className="text-sm text-slate-600 mb-1">Mean X</p>
              <p className="text-3xl font-bold text-blue-700">{statistics.meanX}</p>
            </div>
            <div className="bg-gradient-to-br from-green-100 to-green-50 p-4 rounded-lg border border-green-200">
              <p className="text-sm text-slate-600 mb-1">Mean Y</p>
              <p className="text-3xl font-bold text-green-700">{statistics.meanY}</p>
            </div>
            <div className="bg-gradient-to-br from-purple-100 to-purple-50 p-4 rounded-lg border border-purple-200">
              <p className="text-sm text-slate-600 mb-1">Correlation</p>
              <p className="text-3xl font-bold text-purple-700">{statistics.correlation}</p>
            </div>
            <div className="bg-gradient-to-br from-orange-100 to-orange-50 p-4 rounded-lg border border-orange-200">
              <p className="text-sm text-slate-600 mb-1">Min Y</p>
              <p className="text-3xl font-bold text-orange-700">{statistics.minY}</p>
            </div>
            <div className="bg-gradient-to-br from-red-100 to-red-50 p-4 rounded-lg border border-red-200">
              <p className="text-sm text-slate-600 mb-1">Max Y</p>
              <p className="text-3xl font-bold text-red-700">{statistics.maxY}</p>
            </div>
            <div className="bg-gradient-to-br from-indigo-100 to-indigo-50 p-4 rounded-lg border border-indigo-200">
              <p className="text-sm text-slate-600 mb-1">Sample Size</p>
              <p className="text-3xl font-bold text-indigo-700">{sampleSize}</p>
            </div>
          </div>
          <div className="bg-purple-50 border-l-4 border-purple-500 p-4">
            <p className="text-sm text-slate-700">
              <strong>📍 Variable:</strong> <code className="bg-slate-200 px-2 py-1 rounded font-mono">statistics</code>
            </p>
            <p className="text-sm text-slate-600 mt-2">
              <strong>Dependencies:</strong> Depends on <code className="bg-slate-200 px-2 py-1 rounded font-mono">rawData</code> from Cell 2,
              which depends on <code className="bg-slate-200 px-2 py-1 rounded font-mono">sampleSize</code> from Cell 1
            </p>
          </div>
        </CardContent>
      </Card>

      {/* Cell 4: Dynamic Markdown Output */}
      <Card className="border-2 border-amber-200 shadow-lg">
        <CardHeader className="bg-amber-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-amber-500 text-white px-3 py-1 rounded text-sm font-mono">Cell 4</span>
            Dynamic Analysis Report
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="bg-white p-6 rounded-lg border-2 border-slate-200">
            <h3 className="text-2xl font-bold text-slate-800 mb-4">
              {dynamicContent.sizeCategory}
            </h3>
            
            <p className="text-slate-700 mb-4 leading-relaxed">
              With <strong className="text-blue-600">{sampleSize} data points</strong>, we observe a{' '}
              <strong className="text-purple-600">{dynamicContent.corrStrength}</strong> positive 
              correlation of <strong className="text-green-600">{statistics.correlation}</strong> between 
              variables X and Y.
            </p>
            
            <div className={`border-l-4 p-4 mb-4 ${
              sampleSize < 50 ? 'bg-yellow-50 border-yellow-400' : 'bg-blue-50 border-blue-400'
            }`}>
              <p className={sampleSize < 50 ? 'text-yellow-800' : 'text-blue-800'}>
                <strong>📊 Note:</strong> {dynamicContent.sizeAdvice}
              </p>
            </div>
            
            {parseFloat(statistics.correlation) > 0.8 && (
              <div className="bg-green-50 border-l-4 border-green-400 p-4 mb-4">
                <p className="text-green-800">
                  <strong>✨ Insight:</strong> The high correlation suggests a strong linear 
                  relationship, consistent with our synthetic model y = 2x + 3.
                </p>
              </div>
            )}
            
            <div className="bg-slate-50 p-4 rounded-lg">
              <p className="text-slate-700">
                <strong>Range Analysis:</strong> The Y variable ranges from{' '}
                <span className="font-mono bg-orange-100 px-2 py-1 rounded">{statistics.minY}</span> to{' '}
                <span className="font-mono bg-red-100 px-2 py-1 rounded">{statistics.maxY}</span>, 
                with a mean of <span className="font-mono bg-green-100 px-2 py-1 rounded">{statistics.meanY}</span>.
              </p>
            </div>
          </div>
          
          <div className="bg-amber-50 border-l-4 border-amber-500 p-4 mt-4">
            <p className="text-sm text-slate-700">
              <strong>📍 Variable:</strong> <code className="bg-slate-200 px-2 py-1 rounded font-mono">dynamicContent</code>
            </p>
            <p className="text-sm text-slate-600 mt-2">
              <strong>Dependencies:</strong> This markdown content updates dynamically based on 
              <code className="bg-slate-200 px-2 py-1 rounded font-mono mx-1">statistics</code> from Cell 3 and 
              <code className="bg-slate-200 px-2 py-1 rounded font-mono mx-1">sampleSize</code> from Cell 1
            </p>
          </div>
        </CardContent>
      </Card>

      {/* Data Flow Diagram */}
      <Card className="border-2 border-slate-300 shadow-lg">
        <CardHeader className="bg-slate-100">
          <CardTitle className="flex items-center gap-2">
            📊 Data Flow & Variable Dependencies
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="flex flex-col items-center space-y-3">
            <div className="bg-blue-100 border-2 border-blue-500 rounded-lg p-4 text-center w-64">
              <strong className="text-blue-800">Cell 1: sampleSize</strong>
              <br />
              <span className="text-sm text-slate-600">Interactive Slider Widget</span>
            </div>
            <div className="text-3xl text-blue-500">↓</div>
            <div className="bg-green-100 border-2 border-green-500 rounded-lg p-4 text-center w-64">
              <strong className="text-green-800">Cell 2: rawData</strong>
              <br />
              <span className="text-sm text-slate-600">Generated Dataset (n={sampleSize})</span>
            </div>
            <div className="text-3xl text-green-500">↓</div>
            <div className="bg-purple-100 border-2 border-purple-500 rounded-lg p-4 text-center w-64">
              <strong className="text-purple-800">Cell 3: statistics</strong>
              <br />
              <span className="text-sm text-slate-600">Computed Metrics</span>
            </div>
            <div className="text-3xl text-purple-500">↓</div>
            <div className="bg-amber-100 border-2 border-amber-500 rounded-lg p-4 text-center w-64">
              <strong className="text-amber-800">Cell 4: dynamicContent</strong>
              <br />
              <span className="text-sm text-slate-600">Reactive Markdown Report</span>
            </div>
          </div>
          
          <div className="mt-6 p-4 bg-slate-50 rounded-lg">
            <p className="text-sm text-slate-700 font-semibold mb-2">💡 How It Works:</p>
            <ul className="text-sm text-slate-600 space-y-1 list-disc list-inside">
              <li>Moving the slider changes <code className="bg-slate-200 px-1 rounded">sampleSize</code></li>
              <li>This triggers regeneration of <code className="bg-slate-200 px-1 rounded">rawData</code></li>
              <li>New data triggers recalculation of <code className="bg-slate-200 px-1 rounded">statistics</code></li>
              <li>Updated statistics trigger refresh of <code className="bg-slate-200 px-1 rounded">dynamicContent</code></li>
              <li>All updates happen automatically (reactive computation)</li>
            </ul>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default InteractiveNotebook;