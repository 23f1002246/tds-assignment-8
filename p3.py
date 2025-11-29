import React, { useState } from 'react';
import { Slider } from '@/components/ui/slider';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ScatterChart, Scatter } from 'recharts';

// Email: 23f1002246@ds.study.iitm.ac.in

const MarimoNotebook = () => {
  // Cell 1: Interactive slider widget for sample size
  // This controls how many data points we generate
  const [sampleSize, setSampleSize] = useState(50);
  
  // Cell 2: Generate synthetic dataset based on sample size
  // Data flow: sampleSize -> rawData
  // This cell depends on the slider value from Cell 1
  const generateData = (n) => {
    const data = [];
    for (let i = 0; i < n; i++) {
      const x = i / n * 10;
      // y = 2x + 3 + noise (linear relationship with random variation)
      const y = 2 * x + 3 + (Math.random() - 0.5) * 2;
      data.push({ x: parseFloat(x.toFixed(2)), y: parseFloat(y.toFixed(2)) });
    }
    return data;
  };
  
  const rawData = generateData(sampleSize);
  
  // Cell 3: Calculate statistical measures from the dataset
  // Data flow: rawData -> statistics
  // This cell depends on the generated data from Cell 2
  const calculateStatistics = (data) => {
    const xValues = data.map(d => d.x);
    const yValues = data.map(d => d.y);
    
    const meanX = xValues.reduce((a, b) => a + b, 0) / data.length;
    const meanY = yValues.reduce((a, b) => a + b, 0) / data.length;
    
    // Calculate correlation coefficient
    let numerator = 0;
    let denomX = 0;
    let denomY = 0;
    
    for (let i = 0; i < data.length; i++) {
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
  };
  
  const statistics = calculateStatistics(rawData);

  return (
    <div className="w-full max-w-6xl mx-auto p-6 space-y-6 bg-gradient-to-br from-slate-50 to-blue-50 min-h-screen">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-slate-800 mb-2">
          Interactive Data Analysis Notebook
        </h1>
        <p className="text-slate-600">Demonstrating variable dependencies and reactive computation</p>
      </div>

      {/* Cell 1: Interactive Controls */}
      <Card className="border-2 border-blue-200 shadow-lg">
        <CardHeader className="bg-blue-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-blue-500 text-white px-3 py-1 rounded text-sm">Cell 1</span>
            Interactive Widget - Sample Size Control
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <label className="text-lg font-medium text-slate-700">
                Sample Size: <span className="text-blue-600 font-bold">{sampleSize}</span>
              </label>
              <span className="text-sm text-slate-500">Adjust to see real-time updates</span>
            </div>
            <Slider
              value={[sampleSize]}
              onValueChange={(value) => setSampleSize(value[0])}
              min={10}
              max={200}
              step={10}
              className="w-full"
            />
            <p className="text-sm text-slate-600 bg-slate-100 p-3 rounded">
              💡 <strong>Data Flow:</strong> This slider controls the number of data points generated. 
              Changes here cascade to all dependent cells below.
            </p>
          </div>
        </CardContent>
      </Card>

      {/* Cell 2: Data Visualization */}
      <Card className="border-2 border-green-200 shadow-lg">
        <CardHeader className="bg-green-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-green-500 text-white px-3 py-1 rounded text-sm">Cell 2</span>
            Scatter Plot - Raw Data Visualization
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <ResponsiveContainer width="100%" height={300}>
            <ScatterChart margin={{ top: 20, right: 30, bottom: 20, left: 20 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="x" name="X Variable" label={{ value: 'X', position: 'insideBottom', offset: -10 }} />
              <YAxis dataKey="y" name="Y Variable" label={{ value: 'Y', angle: -90, position: 'insideLeft' }} />
              <Tooltip cursor={{ strokeDasharray: '3 3' }} />
              <Legend />
              <Scatter name="Data Points" data={rawData} fill="#3b82f6" />
            </ScatterChart>
          </ResponsiveContainer>
          <p className="text-sm text-slate-600 bg-slate-100 p-3 rounded mt-4">
            💡 <strong>Dependencies:</strong> This cell depends on <code className="bg-slate-200 px-2 py-1 rounded">sampleSize</code> from Cell 1.
            The data follows the relationship: <code className="bg-slate-200 px-2 py-1 rounded">y = 2x + 3 + noise</code>
          </p>
        </CardContent>
      </Card>

      {/* Cell 3: Statistical Analysis */}
      <Card className="border-2 border-purple-200 shadow-lg">
        <CardHeader className="bg-purple-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-purple-500 text-white px-3 py-1 rounded text-sm">Cell 3</span>
            Statistical Summary
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            <div className="bg-gradient-to-br from-blue-100 to-blue-50 p-4 rounded-lg">
              <p className="text-sm text-slate-600 mb-1">Mean X</p>
              <p className="text-2xl font-bold text-blue-700">{statistics.meanX}</p>
            </div>
            <div className="bg-gradient-to-br from-green-100 to-green-50 p-4 rounded-lg">
              <p className="text-sm text-slate-600 mb-1">Mean Y</p>
              <p className="text-2xl font-bold text-green-700">{statistics.meanY}</p>
            </div>
            <div className="bg-gradient-to-br from-purple-100 to-purple-50 p-4 rounded-lg">
              <p className="text-sm text-slate-600 mb-1">Correlation</p>
              <p className="text-2xl font-bold text-purple-700">{statistics.correlation}</p>
            </div>
            <div className="bg-gradient-to-br from-orange-100 to-orange-50 p-4 rounded-lg">
              <p className="text-sm text-slate-600 mb-1">Min Y</p>
              <p className="text-2xl font-bold text-orange-700">{statistics.minY}</p>
            </div>
            <div className="bg-gradient-to-br from-red-100 to-red-50 p-4 rounded-lg">
              <p className="text-sm text-slate-600 mb-1">Max Y</p>
              <p className="text-2xl font-bold text-red-700">{statistics.maxY}</p>
            </div>
            <div className="bg-gradient-to-br from-indigo-100 to-indigo-50 p-4 rounded-lg">
              <p className="text-sm text-slate-600 mb-1">Sample Size</p>
              <p className="text-2xl font-bold text-indigo-700">{sampleSize}</p>
            </div>
          </div>
          <p className="text-sm text-slate-600 bg-slate-100 p-3 rounded mt-4">
            💡 <strong>Dependencies:</strong> This cell depends on <code className="bg-slate-200 px-2 py-1 rounded">rawData</code> from Cell 2,
            which in turn depends on <code className="bg-slate-200 px-2 py-1 rounded">sampleSize</code> from Cell 1.
          </p>
        </CardContent>
      </Card>

      {/* Cell 4: Dynamic Markdown Output */}
      <Card className="border-2 border-amber-200 shadow-lg">
        <CardHeader className="bg-amber-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-amber-500 text-white px-3 py-1 rounded text-sm">Cell 4</span>
            Dynamic Analysis Report
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6 prose max-w-none">
          <div className="bg-white p-6 rounded-lg border border-slate-200">
            <h3 className="text-xl font-semibold text-slate-800 mb-4">
              {sampleSize < 50 ? '⚠️ Small Sample Analysis' : 
               sampleSize < 100 ? '✓ Medium Sample Analysis' : 
               '✓ Large Sample Analysis'}
            </h3>
            
            <p className="text-slate-700 mb-3">
              With <strong>{sampleSize} data points</strong>, we observe a {' '}
              {parseFloat(statistics.correlation) > 0.9 ? 'very strong' :
               parseFloat(statistics.correlation) > 0.7 ? 'strong' :
               parseFloat(statistics.correlation) > 0.5 ? 'moderate' : 'weak'} positive 
              correlation of <strong>{statistics.correlation}</strong> between variables X and Y.
            </p>
            
            {sampleSize < 50 && (
              <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-3">
                <p className="text-yellow-800">
                  <strong>Note:</strong> Sample size is relatively small. Consider increasing 
                  to at least 50 points for more reliable statistical inference.
                </p>
              </div>
            )}
            
            {parseFloat(statistics.correlation) > 0.8 && (
              <div className="bg-green-50 border-l-4 border-green-400 p-4 mb-3">
                <p className="text-green-800">
                  <strong>Insight:</strong> The high correlation suggests a strong linear 
                  relationship, consistent with our synthetic model y = 2x + 3.
                </p>
              </div>
            )}
            
            <p className="text-slate-700">
              The Y variable ranges from <strong>{statistics.minY}</strong> to{' '}
              <strong>{statistics.maxY}</strong>, with a mean of <strong>{statistics.meanY}</strong>.
            </p>
          </div>
          
          <p className="text-sm text-slate-600 bg-slate-100 p-3 rounded mt-4">
            💡 <strong>Reactive Output:</strong> This markdown content updates dynamically based on 
            <code className="bg-slate-200 px-2 py-1 rounded">statistics</code> from Cell 3 and 
            <code className="bg-slate-200 px-2 py-1 rounded">sampleSize</code> from Cell 1.
          </p>
        </CardContent>
      </Card>

      {/* Data Flow Diagram */}
      <Card className="border-2 border-slate-300 shadow-lg">
        <CardHeader className="bg-slate-100">
          <CardTitle>📊 Data Flow Diagram</CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="flex flex-col items-center space-y-4">
            <div className="bg-blue-100 border-2 border-blue-500 rounded-lg p-4 text-center">
              <strong>Cell 1: sampleSize</strong>
              <br />
              <span className="text-sm text-slate-600">(Interactive Slider)</span>
            </div>
            <div className="text-2xl text-slate-400">↓</div>
            <div className="bg-green-100 border-2 border-green-500 rounded-lg p-4 text-center">
              <strong>Cell 2: rawData</strong>
              <br />
              <span className="text-sm text-slate-600">(Generated Dataset)</span>
            </div>
            <div className="text-2xl text-slate-400">↓</div>
            <div className="bg-purple-100 border-2 border-purple-500 rounded-lg p-4 text-center">
              <strong>Cell 3: statistics</strong>
              <br />
              <span className="text-sm text-slate-600">(Computed Metrics)</span>
            </div>
            <div className="text-2xl text-slate-400">↓</div>
            <div className="bg-amber-100 border-2 border-amber-500 rounded-lg p-4 text-center">
              <strong>Cell 4: Dynamic Report</strong>
              <br />
              <span className="text-sm text-slate-600">(Reactive Markdown)</span>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default MarimoNotebook;