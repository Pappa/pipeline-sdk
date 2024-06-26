
import numpy as np
import pandas as pd

from pipeliner.recommendations.transformer import (
    UserItemMatrixTransformer,
    SimilarityTransformer,
)
from sklearn.pipeline import Pipeline as SKPipeline

data_types = {"user_id": str, "item_id": str, "rating": np.float64}

if __name__ == "__main__":
    base_dir = "/opt/ml/processing"
    data_path = "user_item_ratings.csv"

    user_item_ratings = pd.read_csv(f"{base_dir}/{data_path}", dtype=data_types)

    transformer = SKPipeline(
        [
            ("user_item", UserItemMatrixTransformer()),
            ("similarity", SimilarityTransformer(kind=kind, metric=metric)),
        ]
    )

    similarity_matrix = transformer.transform(user_item_ratings)

    similarity_matrix.to_csv(f"{base_dir}/user_item_similarity_matrix.csv", header=True, index=False)
