// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 列举当前用户收到的共享文件列表
 */
public class ListReceivedFileRequest extends TeaModel {
    // 查询返回的记录数
    @NameInMap("limit")
    @Validation(required = true)
    public Integer limit;

    // 上次查询返回的游标
    @NameInMap("marker")
    public String marker;

    @NameInMap("subdomain_id")
    public String subdomainId;

    public static ListReceivedFileRequest build(java.util.Map<String, ?> map) throws Exception {
        ListReceivedFileRequest self = new ListReceivedFileRequest();
        return TeaModel.build(map, self);
    }

    public ListReceivedFileRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListReceivedFileRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListReceivedFileRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
