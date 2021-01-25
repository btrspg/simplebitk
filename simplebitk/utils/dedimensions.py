# AUTOGENERATED! DO NOT EDIT! File to edit: 00_utils_rd.ipynb (unless otherwise specified).

__all__ = ['reduce_dimensional', 'de_dim_methods']

# Cell

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE, MDS
from phate import PHATE
from umap import UMAP


# Cell

def reduce_dimensional(df,method=PCA,n_components=2):
    if method not in [PCA,MDS,TSNE,UMAP,PHATE]:
        raise ValueError('method should be in [PCA,MDS,TSNE,UMAP,PHATE], not '+str(method))
    prefix=getattr(method,'__name__')

    reducer = method(n_components=n_components,random_state=422)
    results=reducer.fit_transform(df)

    if isinstance(n_components,float):
        n_components = method.n_compnents_
    reduced_df = pd.DataFrame({prefix+str(i+1):results[:,i] for i in range(n_components)})
    return reduced_df,reducer

de_dim_methods = {
    'PCA':PCA,'MDS':MDS,'TSNE':TSNE,'UMAP':UMAP,'PHATE':PHATE
}