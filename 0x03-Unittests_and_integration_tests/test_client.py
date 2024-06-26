#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mocked_get_json):
        """
        Test the org method of GithubOrgClient
        """
        endpoint = 'https://api.github.com/orgs/{}'.format(org_name)
        client = GithubOrgClient(org_name)
        client.org()
        mocked_get_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ('random_url', {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, org_name, response_payload):
        """
        Test the _public_repos_url property of GithubOrgClient
        """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=response_payload)):
            client = GithubOrgClient(org_name)
            self.assertEqual(
                    client._public_repos_url,
                    response_payload.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """
        Test the public_repos method of GithubOrgClient
        """
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public_repos_url:

            mocked_public_repos_url.return_value = "world"
            client = GithubOrgClient('test')
            response = client.public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public_repos_url.assert_called_once()
            mocked_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo_data, license_key, expectation):
        """
        Test the has_license method of GithubOrgClient
        """
        result = GithubOrgClient.has_license(repo_data, license_key)
        self.assertEqual(result, expectation)

@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration tests"""
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class after integration tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public repos retrieval"""

    def test_public_repos_with_license(self):
        """Test public repos with license retrieval"""


if __name__ == '__main__':
    unittest.main()
