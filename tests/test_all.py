from HaloPSA import Halo
import os
import pytest

HALO_TENANT = os.getenv('HALO_TENANT')
HALO_ID = os.getenv('HALO_CLIENT_ID')
HALO_SECRET = os.getenv('HALO_SECRET')

# 
halo = Halo(HALO_TENANT, HALO_ID, HALO_SECRET)

class TestActions:
    def test_search_assets(self):
        assets = halo.Actions.search()
        assert isinstance(assets, dict)
        assert isinstance(assets['record_count'], int)
        assert isinstance(assets['actions'], list)
        
class TestAgents:
    def test_search_assets(self):
        assets = halo.Agents.search()
        assert isinstance(assets, dict)
        assert isinstance(assets['record_count'], int)
        assert isinstance(assets['agents'], list)
        
class TestAssets:
    def test_search_assets(self):
        assets = halo.Assets.search()
        assert isinstance(assets, dict)
        assert isinstance(assets['record_count'], int)
        assert isinstance(assets['assets'], list)
