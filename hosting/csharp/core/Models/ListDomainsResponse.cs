// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * list domain response
     */
    public class ListDomainsResponse : TeaModel {
        /// <summary>
        /// domain 列表
        /// </summary>
        [NameInMap("items")]
        [Validation(Required=false)]
        public List<BaseDomainResponse> Items { get; set; }

        /// <summary>
        /// 下次分页查询游标
        /// </summary>
        [NameInMap("next_marker")]
        [Validation(Required=false)]
        public string NextMarker { get; set; }

    }

}
