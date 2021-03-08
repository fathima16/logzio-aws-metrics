import os

SCRAPE_INTERVAL = f'{os.environ["SCRAPE_INTERVAL"]}s'
aws = {
    'job_name': 'logzio-cloudwatch-metrics',
    'scrape_interval': SCRAPE_INTERVAL,
    'scrape_timeout': SCRAPE_INTERVAL,
    'static_configs': [{
        'targets': ['cloudwatch-exporter:9106'],
        'labels': {'p8s_logzio_name': os.environ['P8S_LOGZIO_NAME']}
    }]
}
