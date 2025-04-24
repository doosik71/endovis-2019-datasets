# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os
import synapseclient
import synapseutils

load_dotenv()

local_folder = "./data"

if not os.path.exists(local_folder):
    os.makedirs(local_folder)

print("Start downloading.")

authToken = os.getenv("SYNAPSE_ACCESS_TOKEN")

if authToken is None:
    raise ValueError("Please set the \"SYNAPSE_ACCESS_TOKEN\" environment variable.")

syn = synapseclient.Synapse()
syn.login(authToken=authToken)

project_id = "syn18779624" # EndoVis 2019 Datasets
synapseutils.syncFromSynapse(syn, entity=project_id, path=local_folder)

print("Finished downloading.")
