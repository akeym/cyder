$(document).ready(function() {
    $('.wizard').live('change', function() {
        var rng;
        var free_ip;
        if(this.id == 'id_range' || (this.id == 'id_next_ip' && $('#id_range').val() != '')) {
            rng = $('#id_range').val();
        } else {
            rng = '';
        };
        if($('#id_next_ip').attr('checked')) {
            free_ip = true;
        } else {
            free_ip = '';
        };
        var postData = {
            vrf: $('#id_vrf').val(),
            site: $('#id_site').val(),
            range: rng,
            free_ip: free_ip,
        };
        if(this.id == 'id_next_ip' && $('#id_range').val() != '' || this.id != 'id_next_ip') {
            $.post('/dhcp/range/range_wizard/', postData, function(data) {
                if(data.ranges) {
                    $('#id_range').find('option').remove().end();
                    for(i in data.ranges[0]) {
                        $('#id_range').find('option').end().append('<option value=' + data.ranges[1][i] + '>' + data.ranges[0][i] + '</option>');
                    };
                };
                if(data.ip_type) {
                    if(data.ip_type == $('#id_ip_type_0').val()) {
                        $('#id_ip_type_0').attr('checked', 'checked');
                    } else {
                        $('#id_ip_type_1').attr('checked', 'checked');
                    };

                    $('#id_ip_str').val(data.ip_str);
                }
            }, 'json');
        };
    });
});
