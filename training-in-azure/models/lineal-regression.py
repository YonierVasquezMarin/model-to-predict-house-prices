import argparse
import mlflow

def main():
    ###########################
    # <Tomar los datos iniciales>
    ###########################
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, help="data cleaned")
    parser.add_argument("--registered_model_name", type=str, help="model name")
    args = parser.parse_args()
    ###########################
    # </Tomar los datos iniciales>
    ###########################

    # Start Logging
    mlflow.start_run()

    # Enable autologging
    mlflow.sklearn.autolog()

    ###############################
    # <Revisar los datos iniciales>
    ###############################
    print("input data:", args.data)
    ################################
    # </Revisar los datos iniciales>
    ################################

    # Stop Logging
    mlflow.end_run()

if __name__ == "__main__":
    main()