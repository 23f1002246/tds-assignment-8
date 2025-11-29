import React, { useState, useMemo } from 'react';
import { Slider } from '@/components/ui/slider';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Line, LineChart } from 'recharts';

const MarimoNotebook = () => {
  // Cell 1: Interactive slider widget
  const [sampleSize, setSampleSize] = useState(50);
  
  // Cell 2: Generate data (depends on sampleSize)
  const rawData = useMemo(() => {
    const data = [];
    for (let i = 0; i < sampleSize; i++) {
      const x = (i / sampleSize) * 10;
      const y = 2 * x + 3 + (Math.random() - 0.5) * 2;
      data.push({ x: parseFloat(x.toFixed(2)), y: parseFloat(y.toFixed(2)) });
    }
    return data;
  }, [sampleSize]);
  
  // Cell 3: Calculate statistics (depends on rawData)
  const statistics = useMemo(() => {
    const xValues = rawData.map(d => d.x);
    const yValues = rawData.map(d => d.y);
    const meanX = xValues.reduce((a, b) => a + b, 0) / rawData.length;
    const meanY = yValues.reduce((a, b) => a + b, 0) / rawData.length;
    
    let numerator = 0, denomX = 0, denomY = 0;
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

  // Cell 4: Dynamic markdown (depends on sampleSize and statistics)
  const analysisText = useMemo(() => {
    const corr = parseFloat(statistics.correlation);
    let sizeStatus, advice, corrStrength;
    
    if (sampleSize < 50) {
      sizeStatus = '⚠️ Small Sample';
      advice = 'Sample size is small. Consider n ≥ 50 for reliable inference.';
    } else if (sampleSize < 100) {
      sizeStatus = '✅ Medium Sample';
      advice = 'Sample size is adequate for basic analysis.';
    } else {
      sizeStatus = '✅ Large Sample';
      advice = 'Sample size is robust for reliable inference.';
    }
    
    if (corr > 0.9) corrStrength = 'very strong';
    else if (corr > 0.7) corrStrength = 'strong';
    else if (corr > 0.5) corrStrength = 'moderate';
    else corrStrength = 'weak';
    
    return { sizeStatus, advice, corrStrength };
  }, [sampleSize, statistics]);

  return (
    <div className="w-full max-w-6xl mx-auto p-6 space-y-6 bg-gradient-to-br from-purple-50 via-blue-50 to-cyan-50 min-h-screen">
      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent mb-2">
          Interactive Marimo Notebook
        </h1>
        <p className="text-slate-600 text-lg">Reactive Data Analysis with Cell Dependencies</p>
        <p className="text-sm text-slate-500 mt-2 font-mono">Email: 23f1002246@ds.study.iitm.ac.in</p>
      </div>

      {/* Cell 1: Interactive Slider */}
      <Card className="border-2 border-purple-300 shadow-xl">
        <CardHeader className="bg-gradient-to-r from-purple-100 to-purple-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-purple-600 text-white px-3 py-1 rounded font-mono text-sm">Cell 1</span>
            <span className="text-purple-900">Interactive Slider Widget</span>
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="space-y-4">
            <div className="flex items-center justify-between mb-2">
              <label className="text-lg font-semibold text-slate-700">
                Sample Size: <span className="text-purple-600 text-3xl font-bold">{sampleSize}</span>
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
            <div className="bg-purple-50 border-l-4 border-purple-500 p-4 rounded">
              <p className="text-sm text-slate-700">
                <span className="font-mono bg-purple-200 px-2 py-1 rounded">sample_size</span> = {sampleSize}
              </p>
              <p className="text-sm text-slate-600 mt-2">
                💡 Drag the slider to update all dependent cells reactively
              </p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Cell 2: Data Table Preview */}
      <Card className="border-2 border-blue-300 shadow-xl">
        <CardHeader className="bg-gradient-to-r from-blue-100 to-blue-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-blue-600 text-white px-3 py-1 rounded font-mono text-sm">Cell 2</span>
            <span className="text-blue-900">Generated Dataset</span>
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="bg-white rounded-lg border border-blue-200 overflow-hidden mb-4">
            <table className="w-full text-sm">
              <thead className="bg-blue-50">
                <tr>
                  <th className="px-4 py-2 text-left font-semibold">Index</th>
                  <th className="px-4 py-2 text-left font-semibold">X</th>
                  <th className="px-4 py-2 text-left font-semibold">Y</th>
                </tr>
              </thead>
              <tbody>
                {rawData.slice(0, 5).map((row, idx) => (
                  <tr key={idx} className="border-t border-blue-100">
                    <td className="px-4 py-2 text-slate-600">{idx}</td>
                    <td className="px-4 py-2 font-mono">{row.x}</td>
                    <td className="px-4 py-2 font-mono">{row.y}</td>
                  </tr>
                ))}
              </tbody>
            </table>
            <div className="bg-blue-50 px-4 py-2 text-xs text-slate-600 border-t border-blue-200">
              Showing 5 of {sampleSize} rows
            </div>
          </div>
          <div className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
            <p className="text-sm text-slate-700">
              <span className="font-mono bg-blue-200 px-2 py-1 rounded">raw_data</span> = DataFrame with {sampleSize} rows
            </p>
            <p className="text-sm text-slate-600 mt-2">
              <strong>Dependencies:</strong> <span className="font-mono bg-purple-200 px-2 py-1 rounded">sample_size</span> from Cell 1
            </p>
            <p className="text-sm text-slate-600 mt-1">
              <strong>Model:</strong> y = 2x + 3 + noise
            </p>
          </div>
        </CardContent>
      </Card>

      {/* Cell 3: Statistics */}
      <Card className="border-2 border-green-300 shadow-xl">
        <CardHeader className="bg-gradient-to-r from-green-100 to-green-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-green-600 text-white px-3 py-1 rounded font-mono text-sm">Cell 3</span>
            <span className="text-green-900">Statistical Summary</span>
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mb-4">
            {Object.entries(statistics).map(([key, value]) => (
              <div key={key} className="bg-gradient-to-br from-green-100 to-green-50 p-4 rounded-lg border-2 border-green-200">
                <p className="text-xs text-slate-600 mb-1 uppercase tracking-wide">{key}</p>
                <p className="text-2xl font-bold text-green-700">{value}</p>
              </div>
            ))}
            <div className="bg-gradient-to-br from-indigo-100 to-indigo-50 p-4 rounded-lg border-2 border-indigo-200">
              <p className="text-xs text-slate-600 mb-1 uppercase tracking-wide">Sample Size</p>
              <p className="text-2xl font-bold text-indigo-700">{sampleSize}</p>
            </div>
          </div>
          <div className="bg-green-50 border-l-4 border-green-500 p-4 rounded">
            <p className="text-sm text-slate-700">
              <span className="font-mono bg-green-200 px-2 py-1 rounded">statistics</span> = computed metrics
            </p>
            <p className="text-sm text-slate-600 mt-2">
              <strong>Dependencies:</strong> <span className="font-mono bg-blue-200 px-2 py-1 rounded">raw_data</span> from Cell 2
            </p>
          </div>
        </CardContent>
      </Card>

      {/* Cell 4: Visualization */}
      <Card className="border-2 border-orange-300 shadow-xl">
        <CardHeader className="bg-gradient-to-r from-orange-100 to-orange-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-orange-600 text-white px-3 py-1 rounded font-mono text-sm">Cell 4</span>
            <span className="text-orange-900">Scatter Plot Visualization</span>
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <ResponsiveContainer width="100%" height={350}>
            <ScatterChart margin={{ top: 20, right: 30, bottom: 20, left: 20 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
              <XAxis dataKey="x" name="X" stroke="#64748b" />
              <YAxis dataKey="y" name="Y" stroke="#64748b" />
              <Tooltip cursor={{ strokeDasharray: '3 3' }} />
              <Legend />
              <Scatter name={`Data Points (n=${sampleSize})`} data={rawData} fill="#f97316" />
            </ScatterChart>
          </ResponsiveContainer>
          <div className="bg-orange-50 border-l-4 border-orange-500 p-4 rounded mt-4">
            <p className="text-sm text-slate-700">
              <span className="font-mono bg-orange-200 px-2 py-1 rounded">plot</span> = scatter visualization
            </p>
            <p className="text-sm text-slate-600 mt-2">
              <strong>Dependencies:</strong> <span className="font-mono bg-blue-200 px-2 py-1 rounded">raw_data</span> from Cell 2
            </p>
          </div>
        </CardContent>
      </Card>

      {/* Cell 5: Dynamic Markdown */}
      <Card className="border-2 border-rose-300 shadow-xl">
        <CardHeader className="bg-gradient-to-r from-rose-100 to-rose-50">
          <CardTitle className="flex items-center gap-2">
            <span className="bg-rose-600 text-white px-3 py-1 rounded font-mono text-sm">Cell 5</span>
            <span className="text-rose-900">Dynamic Markdown Report</span>
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="bg-white p-6 rounded-lg border-2 border-rose-200">
            <h2 className="text-2xl font-bold text-slate-800 mb-4">{analysisText.sizeStatus} Analysis Report</h2>
            
            <h3 className="text-lg font-semibold text-slate-700 mb-2">Summary</h3>
            <p className="text-slate-700 mb-4">
              With <strong className="text-rose-600">{sampleSize} data points</strong>, we observe a{' '}
              <strong className="text-purple-600">{analysisText.corrStrength}</strong> positive correlation of{' '}
              <strong className="text-green-600">{statistics.correlation}</strong> between X and Y.
            </p>
            
            <div className={`border-l-4 p-4 mb-4 rounded ${
              sampleSize < 50 ? 'bg-yellow-50 border-yellow-400' : 'bg-blue-50 border-blue-400'
            }`}>
              <p className={`text-sm ${sampleSize < 50 ? 'text-yellow-800' : 'text-blue-800'}`}>
                💡 <strong>Note:</strong> {analysisText.advice}
              </p>
            </div>
            
            <h3 className="text-lg font-semibold text-slate-700 mb-2">Statistical Results</h3>
            <table className="w-full text-sm mb-4">
              <thead className="bg-slate-100">
                <tr>
                  <th className="px-4 py-2 text-left">Metric</th>
                  <th className="px-4 py-2 text-left">Value</th>
                </tr>
              </thead>
              <tbody>
                <tr className="border-t"><td className="px-4 py-2">Mean X</td><td className="px-4 py-2 font-mono">{statistics.meanX}</td></tr>
                <tr className="border-t"><td className="px-4 py-2">Mean Y</td><td className="px-4 py-2 font-mono">{statistics.meanY}</td></tr>
                <tr className="border-t"><td className="px-4 py-2">Correlation</td><td className="px-4 py-2 font-mono">{statistics.correlation}</td></tr>
                <tr className="border-t"><td className="px-4 py-2">Y Range</td><td className="px-4 py-2 font-mono">{statistics.minY} to {statistics.maxY}</td></tr>
              </tbody>
            </table>
            
            <h3 className="text-lg font-semibold text-slate-700 mb-2">Data Flow</h3>
            <pre className="bg-slate-100 p-4 rounded text-xs overflow-x-auto">
{`Cell 1: sample_size (slider)
        ↓
Cell 2: raw_data (generated data)
        ↓
Cell 3: statistics (computed metrics)
        ↓
Cell 4: plot (visualization)
        ↓
Cell 5: dynamic_report (YOU ARE HERE)`}
            </pre>
          </div>
          <div className="bg-rose-50 border-l-4 border-rose-500 p-4 rounded mt-4">
            <p className="text-sm text-slate-700">
              <span className="font-mono bg-rose-200 px-2 py-1 rounded">dynamic_report</span> = reactive markdown
            </p>
            <p className="text-sm text-slate-600 mt-2">
              <strong>Dependencies:</strong>{' '}
              <span className="font-mono bg-purple-200 px-2 py-1 rounded">sample_size</span> from Cell 1,{' '}
              <span className="font-mono bg-green-200 px-2 py-1 rounded">statistics</span> from Cell 3
            </p>
          </div>
        </CardContent>
      </Card>

      {/* Footer with Instructions */}
      <Card className="border-2 border-slate-300 shadow-xl">
        <CardHeader className="bg-slate-100">
          <CardTitle>🎯 How Marimo Works</CardTitle>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="space-y-3 text-sm text-slate-700">
            <p><strong>✅ Reactive Execution:</strong> Change Cell 1 → All dependent cells update automatically</p>
            <p><strong>✅ No Out-of-Order:</strong> Cells always run in dependency order (reproducible)</p>
            <p><strong>✅ Interactive Widgets:</strong> Slider control with real-time updates</p>
            <p><strong>✅ Dynamic Markdown:</strong> Report adapts to sample size and correlation</p>
            <p><strong>✅ Clear Documentation:</strong> Each cell shows its dependencies</p>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default MarimoNotebook;