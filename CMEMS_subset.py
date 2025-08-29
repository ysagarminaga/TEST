import copernicusmarine
copernicusmarine.subset(
  dataset_id="cmems_obs-oc_atl_bgc-plankton_my_l3-olci-300m_P1D",
  dataset_version="202303",
  variables=["CHL", "CHL_uncertainty", "flags"],
  minimum_longitude=-5,
  maximum_longitude=-1,
  minimum_latitude=44,
  maximum_latitude=48,
  start_datetime="2025-08-18T00:00:00",
  end_datetime="2025-08-19T00:00:00",
  coordinates_selection_method="strict-inside",
  netcdf_compression_level=1,
  disable_progress_bar=True,
)
