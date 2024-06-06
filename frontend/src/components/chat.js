import React, { useState, useEffect } from 'react';
import './Chat.css';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/messages')
      .then(response => response.json())
      .then(data => setMessages(data))
      .catch(error => console.error('Error fetching messages:', error));
  }, []);

  const handleSendMessage = () => {
    if (input.trim() === '') return;

    const newMessage = {
      content: input,
      timestamp: new Date().toISOString(),
    };

    fetch('http://localhost:5000/api/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newMessage),
    })
      .then(response => response.json())
      .then(data => {
        setMessages([...messages, data]);
        setInput('');
      })
      .catch(error => console.error('Error sending message:', error));
  };

  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map((message, index) => (
          <div key={index} className="message">
            <span>{message.content}</span>
            <span className="timestamp">{new Date(message.timestamp).toLocaleTimeString()}</span>
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
}

export default Chat;
