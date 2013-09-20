This is just a Demo!
====================

[See https://github.com/okfn/ckan/issues/1006
Issue has been solved. Might have been a SQLite related problem.]

It demonstrates a problem with the CKAN 3 stages model of editing and storing a
dataset. If you try to add custom metadata in stage 1 __and__ stage 3, the one
in stage 3 does not get stored, if you use 'convert_to_extras'. (see this thread:
http://lists.okfn.org/pipermail/ckan-dev/2013-May/004782.html).

This example simply uses the ckan extension integrated in CKAN
(example_idatasetform) and adds a custom metadata field to stage 3
(templates/package/snippets/package_metadata_fields.html) and to the plugin
class. 
