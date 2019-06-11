const FLAG = process.env.FLAG;
const HOST = process.env.HOST;
const PORT = process.env.PORT;

let express = require('express');
let morgan = require('morgan');

let app = express();
app.use(morgan(':remote-addr :method :url')); // logging
app.use('/', express.static('./'));

class TokenError extends Error {}

app.get('/flag', (req, res) => {
  try {
    let token = req.query.token;

    if (!token)
      throw new TokenError('Not provided.');

    if (token.length > 32)
      throw new TokenError(`Bro, ${token.length} is too long!`);

    if (0 < token.length < 16)
      throw new TokenError('No, please.');
    
  } catch (e) {
    if (e instanceof TokenError) {
      res.send(e.message);
      return;
    }
  }
  
  res.send(FLAG);
});

app.listen(PORT, HOST);
