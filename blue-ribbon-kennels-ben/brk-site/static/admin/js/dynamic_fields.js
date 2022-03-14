// I ADDED TWO OCCURENCES OF POSTMESSAGE IN DateTimeShortCuts.js
jQuery.noConflict();

(function ($) {
    function showHideErrorMsg(el, msg) {
        setTimeout(function () {
            el.children().remove('.error-msg');
        }, 5000);
        return el.append('<p class="error-msg" style=color:red;display:inline-block;>' + msg + '</p>');
    };

    function calcNumDays(startDate, endDate) {
        startDate.setHours(0, 0, 0, 0);
        endDate.setHours(0, 0, 0, 0)

        var millisBetween = Math.round(endDate.getTime() - startDate.getTime());
        var days = millisBetween / (1000 * 3600 * 24);
        return days.toFixed(0);
    };

    function checkDependantReservationType() {
        var reservationType = $('#id_type').val();
        if (reservationType.includes('boarding') == true || reservationType == '') {
            return false;
        }
        else if (reservationType.includes('obedience') == true || reservationType.includes('retriever') == true) {
            return true;
        }
    };

    function showExtendedStay() {
        if (checkDependantReservationType() == true) {
            var extendedStayBoolean = $('.field-extended_stay');
            if (extendedStayBoolean.css('display') == 'none') {
                extendedStayBoolean.css('display', 'block')
            }
        }
    };

    function showHideExtendedStayFields(load = null) {
        $("#id_type, #id_extended_stay").on('change load', function (event) {
            if ($('#id_extended_stay').prop('checked') == true) {
                $('.field-pickup_date').css('display', 'block');
                $('.field-additional_cost').css('display', 'block');
                if ($('#id_pickup_date').val()) {
                    $('.field-overall_cost').css('display', 'block');
                    $('.field-cost').css('display', 'none');
                }
                else {
                    $('.field-overall_cost').css('display', 'none');
                    $('.field-cost').css('display', 'block');
                }
            }
            else {
                clearExtendedStayFields();
                if (checkDependantReservationType() == false) {
                    $('.field-extended_stay').css('display', 'none');
                }
                else {
                    $('.field-extended_stay').css('display', 'block');
                }
                $('.field-pickup_date').css('display', 'none');
                $('.field-additional_cost').css('display', 'none');
                $('.field-overall_cost').css('display', 'none');
                $('.field-cost').css('display', 'block');
            }
        });
        if (load) {
            $("#id_type").trigger('load');
        }
    };

    function calcAdditionalCost(numDays) {
        return Number(numDays) * 25;
    };

    function clearExtendedStayFields() {
        $('#id_pickup_date').val(null);
        $('#id_additional_cost').val(null);
        $('#id_overall_cost').val(null);
        $('.field-cost').css('display', 'block');
        $('.field-overall_cost').css('display', 'none');
    };

    function adjustPickupDateAndCost() {
        if ($('#id_extended_date').prop('checked', true)) {
            if ($('#id_pickup_date').val() != null && $('#id_additional_cost').val() != null) {
                var pickupDate = new Date($('#id_pickup_date').val());
                var endDate = new Date($('#id_end_date').val());
                if (pickupDate <= endDate) {
                    clearExtendedStayFields();
                    showHideErrorMsg($('.field-pickup_date'), 'Please re-enter a pickup date after the training end date.')
                }
                else if (pickupDate > endDate) {
                    var numDays = calcNumDays(endDate, pickupDate);
                    var additionalCost = Number(calcAdditionalCost(numDays));
                    $('.field-overall_cost').css('display', 'block');
                    $('.field-cost').css('display', 'none');
                    $('#id_additional_cost').val(additionalCost);
                    $('#id_overall_cost').val(Number($('#id_cost').val()) + additionalCost);
                }
            }
        }
    };

    function calcCost() {
        var _type = $('#id_type').val()
        var numDays = Number($('#id_number_of_days').val());
        if (_type) {
            $.ajax({
                url: '/reservations/ajax/calc_cost/',
                data: {
                    'type': _type,
                    'numDays': numDays,
                },
                dataType: 'json',
                success: function (data) {
                    $('#id_cost').val(Number(data.total_cost));
                    adjustPickupDateAndCost();
                }
            });
        }

    };

    function setNumDays(elId = null) {
        var startDate = new Date($('#id_start_date').val());
        var endDate = new Date($('#id_end_date').val());
        if (startDate != 'Invalid Date' && endDate != 'Invalid Date') {
            if (startDate < endDate) {
                $('#id_number_of_days').val(Number(Math.round(Math.abs(calcNumDays(startDate, endDate)))));
            }
            else {
                clearFields(elId);
            }
        }
    };

    function triggerSetDaysAndCost(elId = null) {
        setNumDays(elId);
        calcCost();
    };

    function clearFields(elId, reservationTypeChanged = null) {
        if (reservationTypeChanged == null) {
            $(elId).val(null);
        }
        $('#id_number_of_days').val(null);
        $('#id_cost').val(null);
    };

    // function clearDateOnly(startDate, endDate, today) {
    //     if (startDate < today && startDate != null) {
    //         $('#id_start_date').val(null);
    //         var reservationType = $('#id_type').val();
    //         if ((reservationType == 'obedience_training' || reservationType == 'retriever_training') && endDate != null) {
    //             $('#id_end_date').val(null);
    //         }
    //         clearFields('#id_start_date');
    //         showHideErrorMsg($('.field-start_date'), 'The date cannot be a past date.')
    //         return true;
    //     }
    //     else if (endDate < today && endDate != null) {
    //         $('#id_end_date').val(null);
    //         clearFields('#id_end_date');
    //         showHideErrorMsg($('.field-end_date'), 'The date cannot be a past date.')
    //         return true;
    //     }
    //     return false;
    // };

    function formatDate(date) {
        var month = String(Number(date.getMonth()) + 1);
        var day = String(date.getDate());
        var year = String(date.getFullYear());

        if (month.length == 1) {
            month = '0' + month;
        }
        if (day.length == 1) {
            day = '0' + day
        }

        return month + '-' + day + '-' + year;
    };

    function getMinDays() {
        var minDays = 1;
        if ($('#id_type').val().includes('obedience_training')) {
            minDays = 30;
        }
        if ($('#id_type').val().includes('retriever_training')) {
            minDays = 60;
        }
        return minDays;
    };

    function disableEndDate() {
        $('#id_end_date').attr('readonly', true);
        $('#id_end_date').parent().find('.datetimeshortcuts').css('display', 'none');
    };

    function enableEndDate() {
        var el = $('#id_end_date');
        if (el.attr('readonly', false)) {
            el.attr('readonly', false);
            el.parent().find('.datetimeshortcuts').css('display', 'inline-block');
        }
    };

    function autoSetEndDate() {
        if ($('#id_type').val().includes('obedience_training') == true || $('#id_type').val().includes('retriever_training') == true) {
            if ($('#id_start_date').val()) {
                var startDate = new Date($('#id_start_date').val());
                var endDate = new Date(startDate.setDate(startDate.getDate() + getMinDays()));
                $('#id_end_date').val(formatDate(endDate));
                disableEndDate();
                return true;
            }
        }
        return null;
    };

    function checkGreaterEndDate(elId, reservationTypeChanged, startDate, endDate) {
        if (startDate != null && endDate != null) {
            var numDays = Number(calcNumDays(startDate, endDate));

            if (numDays <= 0) {
                if (reservationTypeChanged == null) {
                    clearFields('#id_end_date');
                }
                else {
                    clearFields(elId);
                }
                showHideErrorMsg($('.field-end_date').find('.row'), 'The end date must be greater than the start date.');
                return false;
            }
            return true;
        }
    };

    function checkForValidDateEntry(elId, reservationTypeChanged) {
        if (reservationTypeChanged == null) {
            if (stringToDate($(elId).val()) == null) {
                return false;
            }
            if (stringToDate($(elId).val()) == 'Invalid Date') {
                clearFields(elId);
                showHideErrorMsg($(elId).parents('.form-row'), 'Please enter a valid date.')
                return false;
            }
        }
    };

    function validateDateRequirements(startDate, endDate, elId, reservationTypeChanged = null) {
        var reservationType = $('#id_type').val();

        // Check if date entry is a valid date or if date entry is null.
        var validDate = checkForValidDateEntry(elId, reservationTypeChanged);
        if (validDate == false) {
            return null;
        }

        // Remove date entry if is in the past.
        // var pastDate = clearDateOnly(startDate, endDate, new Date().setHours(0, 0, 0, 0));
        // if (pastDate) {
        //     return null;
        // }

        // Check if end date is greater than start date.
        var greaterEndDate = checkGreaterEndDate(elId, reservationTypeChanged, startDate, endDate);
        if (greaterEndDate == false) {
            return null;
        }

        // Auto set end date
        if (reservationType == 'obedience_training' || reservationType == 'retriever_training') {
            autoSetEndDate();
            showExtendedStay();
        }

        return true;
    };

    function formatReservationType(reservationType) {
        var formattedText = reservationType.split('_')[0] + ' ' + reservationType.split('_')[1];
        return formattedText;
    }

    function stringToDate(stringDate) {

        var date = new Date(stringDate)

        if (stringDate == null || stringDate == '') {
            return null;
        }
        else if (date == 'Invalid Date') {
            return 'Invalid Date';
        }
        else {
            return date;
        }
    };

    function onCalendarClick() {

        // listen for post message from DateTimeShortcuts.js
        window.addEventListener('message', function (event) {

            // get id of changed element and the new date
            var elId = '#' + event.data['id'];
            var date = event.data['date'];

            // get initial date values 
            if (elId.includes('id_start_date') == true || elId.includes('id_end_date') == true) {
                var startDate = new Date($('#id_start_date').val());
                var endDate = new Date($('#id_end_date').val());

                // determine which date was changed and update the variable
                if (elId.includes('id_start_date')) {
                    var startDate = new Date(date);
                }
                else if (elId.includes('id_end_date')) {
                    var endDate = new Date(date);
                }

                var validated = validateDateRequirements(startDate, endDate, elId);
                if (validated == true && $('#id_start_date').val() != null && $('#id_end_date').val() != null && $('#id_start_date').val() != '' && $('#id_end_date').val() != '') {
                    triggerSetDaysAndCost();
                }
            }
            else if (elId.includes('id_pickup_date')) {
                var pickupDate = new Date($('#id_pickup_date').val());
                var endDate = new Date($('#id_end_date').val());

                if (pickupDate <= endDate) {
                    clearExtendedStayFields();
                    showHideErrorMsg($(elId).parents('.form-row'), 'Extend stay pickup date must be after the ' + formatReservationType($('#id_type').val()) + ' end date.')
                }
                else if (pickupDate > endDate) {
                    adjustPickupDateAndCost();
                }
            }
        });
    };

    function onCalendarInputChange() {
        
        $("#id_start_date, #id_end_date, #id_pickup_date").change(function (event) {
            var el = $(event.target);
            var elId = '#' + el.attr('id');

            if (elId.includes('id_start_date')) {
                var validated = validateDateRequirements(stringToDate(el.val()), stringToDate($('#id_end_date').val()), elId = elId);
                if (validated == true && $('#id_start_date').val() != null && $('#id_end_date').val() != null && $('#id_start_date').val() != '' && $('#id_end_date').val() != '') {
                    triggerSetDaysAndCost(elId = '#id_start_date');
                }
            }
            else if (elId.includes('id_end_date')) {
                var validated = validateDateRequirements(stringToDate($('#id_start_date').val()), stringToDate(el.val()), elId = elId);
                if (validated == true && $('#id_start_date').val() != null && $('#id_end_date').val() != null && $('#id_start_date').val() != '' && $('#id_end_date').val() != '') {
                    triggerSetDaysAndCost(elId = '#id_end_date');
                }
            }
            else if (elId.includes('id_pickup_date')) {
                var pickupDate = stringToDate($(elId).val());
                if (pickupDate == 'Invalid Date') {
                    $(elId).val(null);
                    clearExtendedStayFields();
                    showHideErrorMsg($(elId).parents('.form-row'), 'Please enter a valid date.')
                }
            }
        });
    };

    function disableAutoCalculatedFields() {
        $('#id_number_of_days').attr('readonly', true);
        $('#id_cost').attr('readonly', true);
        $('#id_additional_cost').attr('readonly', true);
        $('#id_overall_cost').attr('readonly', true);
    };

    function updateOnTypeChange() {
        $("#id_type").change(function (event) {

            var elId = $(event.target).attr('id');

            if ($(event.target).val()) {
                var startDate = stringToDate($('#id_start_date').val());
                var endDate = stringToDate($('#id_end_date').val());

                if (checkDependantReservationType() == false) {
                    $('#id_extended_stay').prop('checked', false);
                    clearExtendedStayFields();
                    $('.field-extended_stay').css('display', 'none');
                    $('.field-pickup_date').css('display', 'none');
                    $('.field-additional_cost').css('display', 'none');
                    $('.field-overall_cost').css('display', 'none');
                    $('.field-cost').css('display', 'block');
                    enableEndDate();
                    if (startDate != null && startDate != 'Invalid Date' && endDate != null && endDate != 'Invalid Date' && $('#id_start_date').val() != '' && $('#id_end_date').val() != '') {
                        var validated = validateDateRequirements(startDate, endDate, elId, reservationTypeChanged = true);
                        if (validated) {
                            triggerSetDaysAndCost();
                        }
                    }
                }
                else if (checkDependantReservationType() == true) {
                    $('.field-extended_stay').css('display', 'block');
                    if (startDate != null && startDate != 'Invalid Date' && $('#id_start_date').val() != '') {
                        var validated = validateDateRequirements(startDate, endDate, elId, reservationTypeChanged = true);
                        if (validated) {
                            triggerSetDaysAndCost();
                        }
                    }
                }
            }
            else {
                clearFields(elId, reservationTypeChanged = true)
            }
        });
    };

    function onLoad() {
        $(window).on('load', function () {
            disableAutoCalculatedFields();
            onCalendarClick();
            onCalendarInputChange();
            updateOnTypeChange();
            showHideExtendedStayFields(load = true);
        });
    };

    function init() {
        onLoad();
    }; init();

})(django.jQuery);
