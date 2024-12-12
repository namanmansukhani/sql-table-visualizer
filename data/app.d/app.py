from deephaven import read_csv
import deephaven.dtypes as dht

dtypes = {
    'scope': dht.string,
    'source': dht.string,
    'field': dht.string,
    'value': dht.string,
    'updateTime': dht.int64,
    'signature': dht.string,
}

data = (
    read_csv(
        '/data/data/sample-naman.csv',
        header=dtypes,
        headless=True,
    )
    .update(
        "updateTime = epochSecondsToInstant(updateTime)"
    )
)