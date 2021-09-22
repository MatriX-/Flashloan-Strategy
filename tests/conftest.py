import pytest
from scripts.tokens import tokens, curve_tokens


@pytest.fixture(autouse=True)
def setup(module_isolation):
    """
    Isolation setup fixture.

    This ensures that each test runs against the same base environment.
    """
    pass


@pytest.fixture(scope="module")
def aave_lending_pool_v2(Contract):
    """
    Yield a `Contract` object for the Aave lending pool address provider.
    """
    yield Contract("0xd05e3E715d945B59290df0ae8eF85c1BdB684744")


@pytest.fixture(scope="module")
def acct(accounts):
    yield accounts.at('0xe7804c37c13166fF0b37F5aE0BB07A3aEbb6e245', force=True)


@pytest.fixture(scope="module")
def flashloan_v2(FlashloanV2, aave_lending_pool_v2, acct):
    """
    Deploy a `Flashloan` contract from `web3.eth.accounts[0]` and yields the
    generated object.
    """
    yield FlashloanV2.deploy(aave_lending_pool_v2, {"from": acct})

@pytest.fixture(scope="module")
def set_tokens(acct, flashloan_v2):
    flashloan_v2.setTokens(
        tokens['dai'],
        curve_tokens['dai'],
        tokens['usdc'],
        curve_tokens['usdc'],
        {'from': acct}
    )
    assert flashloan_v2.tokensSet()

@pytest.fixture(scope="module")
def WMATIC(Contract):
    yield Contract(tokens['wmatic'])


@pytest.fixture(scope="module")
def USDC(Contract):
    yield Contract(tokens['usdc'])


@pytest.fixture(scope="module")
def DAI(Contract):
    yield Contract(tokens['dai'])

@pytest.fixture(scope="module")
def router(interface):
    yield interface.IUniswapRouterV2("0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff")