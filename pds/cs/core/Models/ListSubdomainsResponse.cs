// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class ListSubdomainsResponse : TeaModel {
        /// <summary>
        /// 分页的 subdomain 数据
        /// </summary>
        [NameInMap("items")]
        [Validation(Required=true)]
        public List<BaseSubdomainResponse> Items { get; set; }

        /// <summary>
        /// 分页游标，可以用作下次list的起点
        /// </summary>
        [NameInMap("next_marker")]
        [Validation(Required=true)]
        public string NextMarker { get; set; }

    }

}
