import logging

def setup_logging(level=logging.DEBUG, logger_name='my_game'):
    # Create or get a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)  # Set the logging level for this logger

    # Check if handlers are already added to avoid adding multiple handlers
    if not logger.handlers:
        # Create a console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)  # Set the logging level for this handler

        # Create a formatter and set it for the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(ch)

    return logger

#debug info warning error critical

ent_logger = setup_logging(logging.INFO, "ENTITIES")
desc_logger = setup_logging(logging.INFO, "DESCRIPTIONS")
app_logger = setup_logging(logging.INFO, "MAIN")