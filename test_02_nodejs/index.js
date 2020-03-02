const HTTP = require('http');
const UPSTREAM_URL = 'http://3.95.249.36:8000/';

const server = HTTP.createServer((request, response) => {
  HTTP.get(UPSTREAM_URL, (upstreamResponse) => {
    let bytes = Buffer.from('');

    upstreamResponse.on('data', (data) => {
      bytes = Buffer.concat([bytes, data]);
    });

    upstreamResponse.on('end', () => {
      const data = JSON.parse(bytes);

      response.setHeader('Content-Length', Buffer.byteLength(data[0].guid));
      response.writeHead(200);
      response.end(data[0].guid);
    });
  }).on('error', (e, abc) => {
    response.setHeader('Content-Length', 0);
    response.writeHead(400);
    response.end();
  });
});

server.listen(8000);

