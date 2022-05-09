from brownie import accounts
from scripts.deploy import deploy_simple_storage


def test_can_set_number():
    #* Arrange
    simple_storage = deploy_simple_storage()
    account = accounts[0]
    expected = 777

    #* Act
    tx = simple_storage.setNumber(expected, {"from": account})
    tx.wait(1)

    #* Assert
    assert simple_storage.number() == expected
    