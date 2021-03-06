<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * list cors rule request.
 */
class SetCorsRuleListRequest extends Model
{
    /**
     * @description cors rule list
     *
     * @var CorsRule[]
     */
    public $corsRuleList;

    /**
     * @description domain ID
     *
     * @example sz100
     *
     * @var string
     */
    public $domainId;
    protected $_name = [
        'corsRuleList' => 'cors_rule_list',
        'domainId'     => 'domain_id',
    ];

    public function validate()
    {
        Model::validateRequired('corsRuleList', $this->corsRuleList, true);
        Model::validateRequired('domainId', $this->domainId, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->corsRuleList) {
            $res['cors_rule_list'] = [];
            if (null !== $this->corsRuleList && \is_array($this->corsRuleList)) {
                $n = 0;
                foreach ($this->corsRuleList as $item) {
                    $res['cors_rule_list'][$n++] = null !== $item ? $item->toMap() : $item;
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
     * @return SetCorsRuleListRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['cors_rule_list'])) {
            if (!empty($map['cors_rule_list'])) {
                $model->corsRuleList = [];
                $n                   = 0;
                foreach ($map['cors_rule_list'] as $item) {
                    $model->corsRuleList[$n++] = null !== $item ? CorsRule::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['domain_id'])) {
            $model->domainId = $map['domain_id'];
        }

        return $model;
    }
}
