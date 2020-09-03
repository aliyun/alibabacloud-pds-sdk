// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class ListAppsResponse : TeaModel {
        /// <summary>
        /// App 列表
        /// </summary>
        [NameInMap("items")]
        [Validation(Required=true)]
        public List<GetAppResponse> Items { get; set; }

        /// <summary>
        /// App 分批查询游标
        /// </summary>
        [NameInMap("next_marker")]
        [Validation(Required=false)]
        public string NextMarker { get; set; }

    }

}
