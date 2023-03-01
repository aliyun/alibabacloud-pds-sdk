// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * List my drive request
 */
public class ListMyDriveRequest extends TeaModel {
    /**
     * <p>每页大小限制</p>
     */
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    /**
     * <p>翻页标记, 接口返回的标记值</p>
     */
    @NameInMap("marker")
    public String marker;

    public static ListMyDriveRequest build(java.util.Map<String, ?> map) throws Exception {
        ListMyDriveRequest self = new ListMyDriveRequest();
        return TeaModel.build(map, self);
    }

    public ListMyDriveRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListMyDriveRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
