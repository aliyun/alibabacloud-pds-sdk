// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * list_share_link request
 */
public class ListShareLinkRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // creator
    @NameInMap("creator")
    public String creator;

    // limit
    @NameInMap("limit")
    public Integer limit;

    // marker
    @NameInMap("marker")
    public String marker;

    public static ListShareLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        ListShareLinkRequest self = new ListShareLinkRequest();
        return TeaModel.build(map, self);
    }

    public ListShareLinkRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListShareLinkRequest setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public ListShareLinkRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListShareLinkRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
