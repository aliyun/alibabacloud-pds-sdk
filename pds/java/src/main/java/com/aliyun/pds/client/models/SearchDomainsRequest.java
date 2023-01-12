// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * search domain request
 */
public class SearchDomainsRequest extends TeaModel {
    /**
     * <p>通过购买的实例ID搜索domain</p>
     */
    @NameInMap("instance_id")
    public String instanceId;

    /**
     * <p>分页大小</p>
     */
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    /**
     * <p>查询游标</p>
     */
    @NameInMap("marker")
    public String marker;

    /**
     * <p>domain名称，模糊匹配</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>排序规则</p>
     */
    @NameInMap("order_by")
    public String orderBy;

    /**
     * <p>通过不同ServiceCode搜索</p>
     */
    @NameInMap("service_code")
    public String serviceCode;

    public static SearchDomainsRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchDomainsRequest self = new SearchDomainsRequest();
        return TeaModel.build(map, self);
    }

    public SearchDomainsRequest setInstanceId(String instanceId) {
        this.instanceId = instanceId;
        return this;
    }
    public String getInstanceId() {
        return this.instanceId;
    }

    public SearchDomainsRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SearchDomainsRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SearchDomainsRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public SearchDomainsRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

    public SearchDomainsRequest setServiceCode(String serviceCode) {
        this.serviceCode = serviceCode;
        return this;
    }
    public String getServiceCode() {
        return this.serviceCode;
    }

}
