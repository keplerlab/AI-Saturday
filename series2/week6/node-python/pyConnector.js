const spawn = require('child_process').spawn;
const path = require('path');

const zerorpc = require('zerorpc');
const utils = require('./utils.js');

// TODO: Should go to a config file
const TIMEOUT = 60; // in seconds (adjust as per how long your server calls can take)
const IP = '127.0.0.1';
const PORT = '4242';

class pyConnector {
    static server() {
        if (!pyConnector.connected) {
            console.log('pyConnector – making a new connection to the python layer ..');
            pyConnector.zerorpcProcess = spawn('python', ['-u', path.join(__dirname, 'pyServer.py')]);
            pyConnector.zerorpcProcess.stdout.on('data', function(data) {
                console.info('python:', data.toString());
            });
            pyConnector.zerorpcProcess.stderr.on('data', function(data) {
                console.error('python:', data.toString());
            });

            pyConnector.zerorpc = new zerorpc.Client({'timeout': TIMEOUT, 'heartbeatInterval': TIMEOUT*1000});
            pyConnector.zerorpc.connect('tcp://' + IP + ':' + PORT);
            pyConnector.connected = true;
        }

        return pyConnector.zerorpc;
    }

    static async invoke(method, ...args) {
        var zerorpc = pyConnector.server();
        return await utils.promisify(zerorpc.invoke, zerorpc, method, ...args);
    }
}

module.exports = pyConnector;
