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
    public class ListStoresResponse : TeaModel {
        /// <summary>
        /// Store 列表
        /// </summary>
        [NameInMap("items")]
        [Validation(Required=true)]
        public List<Store> Items { get; set; }

    }

}
