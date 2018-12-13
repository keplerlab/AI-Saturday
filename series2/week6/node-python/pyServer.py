from __future__ import print_function
import zerorpc
from test_python import test_me
from model_load import FastaiImageClassifier
import config

C = config.Config()

PORT = C.PORT

class pyServer(object):
    def listen(self):
        print("Python server started. Listening on {} ..".format(PORT))

    def test(self, param):
        return test_me(param)

    def predict_from_img(self, img_path):
        model = FastaiImageClassifier()
        return model.predict(img_path)

def main():
    try:
        server = zerorpc.Server(pyServer())
        server.bind(f"tcp://0.0.0.0:{PORT}")
        server.run()
        print("Python server running ..")
    except Exception as e:
        print("Unable to start Python server: ", e)
        raise e

if __name__ == "__main__":
    main()
