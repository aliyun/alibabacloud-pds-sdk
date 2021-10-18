// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 列举用户管理的共享文件列表
 */
public class ListMangeSharingFileRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // 查询的用户列表，传入用户ID列表，不传默认查询所有有权限管理的共享
    @NameInMap("creator_list")
    public java.util.List<String> creatorList;

    // 查询返回的记录数
    @NameInMap("limit")
    @Validation(required = true)
    public Integer limit;

    // 上次查询返回的游标
    @NameInMap("marker")
    public String marker;

    public static ListMangeSharingFileRequest build(java.util.Map<String, ?> map) throws Exception {
        ListMangeSharingFileRequest self = new ListMangeSharingFileRequest();
        return TeaModel.build(map, self);
    }

    public ListMangeSharingFileRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ListMangeSharingFileRequest setCreatorList(java.util.List<String> creatorList) {
        this.creatorList = creatorList;
        return this;
    }
    public java.util.List<String> getCreatorList() {
        return this.creatorList;
    }

    public ListMangeSharingFileRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListMangeSharingFileRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
