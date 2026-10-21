import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class SkillSourceTest(unittest.TestCase):
 def test_shared_source_and_no_fake_connection(self):
  meta=json.loads((ROOT/'SOURCE.json').read_text());content=(ROOT/'SKILL.md').read_bytes()
  self.assertEqual(hashlib.sha256(content).hexdigest(),meta['sha256'])
  self.assertTrue(content.startswith(b'---\nname: itpay-services\n'))
  self.assertIn(b'connected ItPay MCP',content)
  self.assertFalse((ROOT/'plugin.json').exists())
  self.assertFalse((ROOT/'mcp.json').exists())
  self.assertFalse((ROOT/'vendor').exists())
