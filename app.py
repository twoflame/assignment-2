import streamlit as st
import pandas as pd
import gzip
import pickle

with gzip.open("healthy_meals_pipeline.pkl.gz", "rb") as f:
    pipeline = pickle.load(f)
