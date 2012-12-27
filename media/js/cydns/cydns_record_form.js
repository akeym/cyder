$(document).ready(function() {
    var cydns = $('#cydns-record');
    var form = $('#cydns-record-form form')[0];
    var recordType = cydns.attr('data-recordType');
    var prettyRecordType = cydns.attr('data-prettyRecordType');
    var searchUrl = cydns.attr('data-searchUrl');
    var getUrl = cydns.attr('data-getUrl');
    var domainsUrl = cydns.attr('data-domainsUrl');

    // For inputs with id = 'id_fqdn' | 'id_target' | server, make smart names.
    make_smart_name_get_domains($('#id_fqdn, #id_target, #id_server'), true, domainsUrl);

    // Record-search dialogs to find records to update.
    $('#record-search').click(function() {
        $('#search-dialog').dialog({
            title: 'Search for a ' + prettyRecordType + ' to update or delete.',
            autoShow: false,
            minWidth: 520,
            buttons: {
                'Cancel': function() {
                    $('#search-dialog').attr('pk', ''),
                    $(this).dialog('close');
                },
                'Edit Record': function() {
                    // To edit. get pk (from when selected from the
                    // dropdown, and request object's form to replace current one.
                    var pk = $(this).attr('pk');
                    $.get(getUrl, {'record_type': recordType, 'pk': pk}, function(data) {
                        $('#record-form-title').html('Updating a ' + prettyRecordType);
                        $('.delete').show();

                        // Populate form with object and set its URL.
                        $('.inner-form').empty().append(data.form);
                        initForms();
                        form.action = '?action=update&pk=' + data.pk;
                        $('#cydns-record-form').slideDown();
                        $('#record-searchbox').attr('value', '');
                    }, 'json');
                    $(this).dialog('close');
                }
            }
        }).show();
    });
    $('#record-search-soa').click(function() {
        $('#search-soa-dialog').dialog({
            title: 'Search for a BIND file',
            autoShow: true,
            minWidth: 520,
            buttons: {
                'Cancel': function() {
                    $('#search-soa-dialog').attr('pk', ''),
                    $(this).dialog('close');
                },
                'View ZONE file': function() {
                    // To edit. get pk (from when selected from the
                    // dropdown, and request object's form to replace current one.
                    window.open('/cydns/bind/build_debug/' +
                                $(this).attr('pk') + '/');
                    $(this).dialog('close');
                }
            }
        }).show();
    });

    // Auto complete for search dialogs.
    $('#record-searchbox').autocomplete({
        // Bind autocomplete to the search field for the specifc record type.
        minLength: 1,
        source: searchUrl + '?record_type=' + recordType,
        select: function( event, ui ) {
            // Save the selected pk so we can use it if the user decides to edit the record.
            $('#search-dialog').attr('pk', ui.item.pk);
        }
    });
    $('#soa-searchbox').autocomplete({
        minLength: 1,
        source: searchUrl + '?record_type=SOA',
        select: function( event, ui ) {
            // Save the selected pk so we can use it if the user decides to edit the record.
            $('#search-soa-dialog').attr('pk', ui.item.pk);
        }
    });

    // Show create form on clicking create button.
    $('#record-create').click(function() {
        $('#record-form-title').html('Creating a ' + prettyRecordType);
        $('.delete').hide();

        clear_form_all(form);
        form.action = '?action=create';
        $('#cydns-record-form').slideDown();
    });
});