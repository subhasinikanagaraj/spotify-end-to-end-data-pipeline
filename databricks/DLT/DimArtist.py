from pyspark import pipelines as dp

@dp.table
def dimartist_stg():
    df = spark.read.table("spotify.silver.dimartist")
    return df

dp.create_streaming_table("dimartist")

dp.create_auto_cdc_flow(
  target = "dimartist",
  source = "dimartist_stg",
  keys = ["artist_id"],
  sequence_by = "updated_at",
  stored_as_scd_type = 2,
  track_history_column_list = None,
  track_history_except_column_list = None,
  name = None,
  once = False
)