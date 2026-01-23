from pyspark import pipelines as dp

@dp.table
def factStream_stg():
    df = spark.read.table("spotify.silver.factStream")
    return df

dp.create_streaming_table("factStream")

dp.create_auto_cdc_flow(
  target = "factStream",
  source = "factStream_stg",
  keys = ["stream_id"],
  sequence_by = "stream_timestamp",
  stored_as_scd_type = 1,
  track_history_column_list = None,
  track_history_except_column_list = None,
  name = None,
  once = False
)