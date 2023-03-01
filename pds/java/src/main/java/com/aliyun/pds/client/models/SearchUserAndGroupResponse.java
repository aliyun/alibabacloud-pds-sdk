// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Search user and group response
 */
public class SearchUserAndGroupResponse extends TeaModel {
    @NameInMap("groups")
    public java.util.List<BaseGroupResponse> groups;

    /**
     * <p>翻页标记</p>
     */
    @NameInMap("next_marker")
    public String nextMarker;

    @NameInMap("users")
    public java.util.List<BaseUserResponse> users;

    public static SearchUserAndGroupResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchUserAndGroupResponse self = new SearchUserAndGroupResponse();
        return TeaModel.build(map, self);
    }

    public SearchUserAndGroupResponse setGroups(java.util.List<BaseGroupResponse> groups) {
        this.groups = groups;
        return this;
    }
    public java.util.List<BaseGroupResponse> getGroups() {
        return this.groups;
    }

    public SearchUserAndGroupResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

    public SearchUserAndGroupResponse setUsers(java.util.List<BaseUserResponse> users) {
        this.users = users;
        return this;
    }
    public java.util.List<BaseUserResponse> getUsers() {
        return this.users;
    }

}
