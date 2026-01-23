from pyspark import pipelines as dp

@dp.table
def dimtrack_stg():
    df = spark.read.table("spotify.silver.DimTrack")
    return df

dp.create_streaming_table("dimtrack")

dp.create_auto_cdc_flow(
  target = "dimtrack",
  source = "dimtrack_stg",
  keys = ["track_id"],
  sequence_by = "updated_at",
  stored_as_scd_type = 2,
  track_history_column_list = None,
  track_history_except_column_list = None,
  name = None,
  once = False
)