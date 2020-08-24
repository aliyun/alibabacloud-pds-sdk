<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class DomainCNameResponse extends Model
{
    /**
     * @description data cname list
     *
     * @var array
     */
    public $dataCnameList;

    /**
     * @description domain ID
     *
     * @example sz100
     *
     * @var string
     */
    public $domainId;
    protected $_name = [
        'dataCnameList' => 'data_cname_list',
        'domainId'      => 'domain_id',
    ];

    public function validate()
    {
        Model::validateRequired('dataCnameList', $this->dataCnameList, true);
        Model::validateRequired('domainId', $this->domainId, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->dataCnameList) {
            $res['data_cname_list'] = [];
            if (null !== $this->dataCnameList && \is_array($this->dataCnameList)) {
                $n = 0;
                foreach ($this->dataCnameList as $item) {
                    $res['data_cname_list'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return DomainCNameResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['data_cname_list'])) {
            if (!empty($map['data_cname_list'])) {
                $model->dataCnameList = [];
                $n                    = 0;
                foreach ($map['data_cname_list'] as $item) {
                    $model->dataCnameList[$n++] = null !== $item ? DataCName::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['domain_id'])) {
            $model->domainId = $map['domain_id'];
        }

        return $model;
    }
}
