const websocket = new WebSocket('wss://localhost:8080');

websocket.onopen = () => {
  console.log('Connected to WebSocket server');
  // Send a message to the server
  websocket.send(JSON.stringify({ text: 'Hello, WebSocket!' }));
};

websocket.onerror = (error) => {
  console.error('WebSocket error:', error);
};

websocket.onmessage = (event) => {
  const message = JSON.parse(event.data);
  console.log(`Received message: ${message.text}`);
};

websocket.onclose = () => {
  console.log('Disconnected from WebSocket server');
};