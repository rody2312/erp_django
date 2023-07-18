def page_name(request):
    page_mapping = {
        'cliente_list': 'cliente',
        'cliente_detail': 'cliente',
        'cliente_new': 'cliente',
        'cliente_edit': 'cliente',

        'proveedor_list': 'proveedor',
        'proveedor_detail': 'proveedor',
        'proveedor_new': 'proveedor',
        'proveedor_edit': 'proveedor',

        'oportunidad_list': 'oportunidad',
        'oportunidad_detail': 'oportunidad',
        'oportunidad_new': 'oportunidad',
        'oportunidad_edit': 'oportunidad',

        'cotizacion_list': 'cotizacion',
        'cotizacion_detail': 'cotizacion',
        'cotizacion_new': 'cotizacion',
        'cotizacion_edit': 'cotizacion',

        'venta_list': 'venta',
        'venta_detail': 'venta',
        'venta_new': 'venta',
        'venta_edit': 'venta',
    }

    view_name = request.resolver_match.view_name
    page_name = page_mapping.get(view_name, '')

    return {'page_name': page_name}