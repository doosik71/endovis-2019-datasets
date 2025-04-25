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

synapse_access_token = os.getenv("SYNAPSE_ACCESS_TOKEN")
project_id = os.getenv("PROJECT_ID")

if synapse_access_token is None:
    raise ValueError('Please set the "SYNAPSE_ACCESS_TOKEN" environment variable.')

if project_id is None:
    raise ValueError('Please set the "PROJECT_ID" environment variable.')

syn = synapseclient.Synapse()
syn.login(authToken=synapse_access_token)

synapseutils.syncFromSynapse(syn, entity=project_id, path=local_folder)

print("Finished downloading.")
