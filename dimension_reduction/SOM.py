import susi
from susi.SOMPlots import plot_umatrix

def SelfOrganisedMap(data, n_rows=30, n_columns=30):
    som = susi.SOMClustering(
                            n_rows,
                            n_columns
                            )
    som.fit(data)
    reduced_data = som.get_clusters(data)
    return reduced_data
