import bin
import logging

def main():
    logging.basicConfig(level='INFO')
    logging.info("Starting Program")
    logging.info("Load Config File")
    bin.Config_Handler.load_file("config.yaml")
    logging.info("Creating Request Manager")
    a = bin.ReqManager()
    logging.info("Creating Command Executor")

    command_executor = bin.CommandExecutor()
    logging.info("Starting Main Loop")
    while True:
        command = a.wait_for_command()
        command_executor.execute(command)


if __name__ == "__main__":
    main()
    time.sleep(200)
