import { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const analyzeSentiment = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;

    setLoading(true);
    setError('');
    setAnalysis(null);

    try {
      const response = await fetch('https://sentiment-analysis-project-75zy.onrender.com/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error('Analysis failed');
      }

      const data = await response.json();
      setAnalysis(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const getSentimentColor = (sentiment) => {
    switch (sentiment?.toLowerCase()) {
      case 'positive': return '#10B981';
      case 'negative': return '#EF4444';
      case 'neutral': return '#6B7280';
      default: return '#6B7280';
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>AI Sentiment Analyzer</h1>
        <p>Analyze the sentiment of your text instantly</p>
      </header>

      <main className="app-main">
        <form className="analysis-form" onSubmit={analyzeSentiment}>
          <div className="textarea-container">
            <textarea
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Enter your text here to analyze sentiment..."
              rows="6"
              disabled={loading}
            />
          </div>
          
          <button 
            type="submit" 
            className="analyze-btn"
            disabled={loading || !text.trim()}
          >
            {loading ? 'Analyzing...' : 'Analyze Sentiment'}
          </button>
        </form>

        {error && (
          <div className="error-message">
            ❌ {error}
          </div>
        )}

        {analysis && (
          <div className="analysis-result">
            <div className="sentiment-badge" style={{ backgroundColor: getSentimentColor(analysis.sentiment) }}>
              {analysis.sentiment.toUpperCase()}
            </div>
            
            <div className="result-details">
              <p><strong>Confidence:</strong> {(analysis.confidence * 100).toFixed(1)}%</p>
              {analysis.score && (
                <p><strong>Score:</strong> {analysis.score.toFixed(4)}</p>
              )}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;