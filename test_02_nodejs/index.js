const fastify = require('fastify')({ logger: true })
const nodeFetch = require('node-fetch');

fastify.get(
  '/', 
  async (request, reply) => {
    const guid = await nodeFetch('http://3.95.249.36:8000/')
      .then(res => res.json())
      .then(json => json[0].guid);

    console.log(guid);
    reply.send(guid);
  }
);


fastify.listen(8000);
