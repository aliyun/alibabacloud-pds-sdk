// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * list_file_by_anonymous request
 */
public class ListByAnonymousRequest extends TeaModel {
    // limit
    @NameInMap("limit")
    public Long limit;

    // marker
    @NameInMap("marker")
    public String marker;

    // parent_file_id
    @NameInMap("parent_file_id")
    @Validation(required = true, pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 4)
    public String parentFileId;

    // share_id
    @NameInMap("share_id")
    @Validation(required = true)
    public String shareId;

    public static ListByAnonymousRequest build(java.util.Map<String, ?> map) throws Exception {
        ListByAnonymousRequest self = new ListByAnonymousRequest();
        return TeaModel.build(map, self);
    }

    public ListByAnonymousRequest setLimit(Long limit) {
        this.limit = limit;
        return this;
    }
    public Long getLimit() {
        return this.limit;
    }

    public ListByAnonymousRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListByAnonymousRequest setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

    public ListByAnonymousRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
