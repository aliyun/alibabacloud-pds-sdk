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
    public class Actor : TeaModel {
        [NameInMap("ali_user")]
        [Validation(Required=false)]
        public ActorAliUser AliUser { get; set; }

        [NameInMap("anonymous_user")]
        [Validation(Required=false)]
        public ActorAnonymousUser AnonymousUser { get; set; }

        [NameInMap("system")]
        [Validation(Required=false)]
        public ActorSystem System { get; set; }

        [NameInMap("user")]
        [Validation(Required=false)]
        public ActorUser User { get; set; }

    }

}
